import os
import re
import json
import html
import time
try:
    import arxiv
except ImportError:
    arxiv = None
import yaml
import logging
import argparse
import datetime
import requests

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

github_url = "https://api.github.com/search/repositories"
arxiv_url = "https://arxiv.org/"

# arxiv.org's CDN rejects the default arxiv.py User-Agent with HTTP 406.
# Using a browser-like UA + explicit Accept header works around it.
ARXIV_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

def make_arxiv_client(delay_seconds: float = 5.0, num_retries: int = 5):
    """Create an arxiv.Client with a patched session that sends a browser-like
    User-Agent and explicit Accept header so arxiv.org doesn't return HTTP 406."""
    if arxiv is None:
        raise RuntimeError("Missing dependency: install the 'arxiv' package to fetch papers.")
    client = arxiv.Client(delay_seconds=delay_seconds, num_retries=num_retries)
    session = getattr(client, "_session", None)
    if session is not None:
        session.headers.update({
            "User-Agent": ARXIV_USER_AGENT,
            "Accept": "application/atom+xml,application/xml;q=0.9,*/*;q=0.8",
        })
    return client

def load_config(config_file:str) -> dict:
    '''
    config_file: input config file path
    return: a dict of configuration
    '''
    # make filters pretty
    def pretty_filters(**config) -> dict:
        keywords = dict()
        EXCAPE = '\"'
        QUOTA = '' # NO-USE
        OR = 'OR' # TODO
        def parse_filters(filters:list):
            ret = ''
            for idx in range(0,len(filters)):
                filter = filters[idx]
                if len(filter.split()) > 1:
                    ret += (EXCAPE + filter + EXCAPE)  
                else:
                    ret += (QUOTA + filter + QUOTA)   
                if idx != len(filters) - 1:
                    ret += OR
            return ret
        for k,v in config['keywords'].items():
            keywords[k] = parse_filters(v['filters'])
        return keywords
    with open(config_file,'r') as f:
        config = yaml.load(f,Loader=yaml.FullLoader) 
        config['kv'] = pretty_filters(**config)
        logging.info(f'config = {config}')
    return config 

def get_authors(authors, first_author = False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output
def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output    

def sort_papers_by_date(papers: dict):
    items = list(papers.items())
    def sort_key(item):
        paper_id, paper = item
        date_value = get_paper_date(paper)
        return (date_value or datetime.date.min, paper_id)
    items.sort(key=sort_key, reverse=True)
    return items

def backfill_web_abstracts(filename,
                           topic_merge=None,
                           topic_drop=None,
                           allowed_topics=None,
                           max_total=0,
                           chunk_size=40,
                           sleep_seconds=1.0):
    with open(filename, "r") as f:
        content = f.read()
        data = json.loads(content) if content else {}
    data = normalize_topics(
        data,
        topic_merge or {},
        topic_drop or [],
        allowed_topics or []
    )

    to_fetch = []
    for topic, papers in data.items():
        for paper_id, paper in papers.items():
            paper_dict = paper_to_dict(paper_id, paper)
            papers[paper_id] = paper_dict
            if paper_dict.get("summary"):
                continue
            to_fetch.append((topic, paper_id))

    if not to_fetch:
        logging.info("No missing abstracts to backfill.")
        return

    if max_total and len(to_fetch) > max_total:
        to_fetch = to_fetch[:max_total]

    logging.info(f"Backfilling abstracts for {len(to_fetch)} papers.")

    for idx in range(0, len(to_fetch), chunk_size):
        chunk = to_fetch[idx:idx + chunk_size]
        ids = [paper_id for _, paper_id in chunk]
        try:
            results = fetch_arxiv_metadata(ids)
        except Exception as exc:
            logging.warning(f"Abstract backfill failed: {exc}")
            break
        for topic, paper_id in chunk:
            result = results.get(paper_id)
            if not result:
                continue
            papers = data.get(topic, {})
            paper_dict = papers.get(paper_id, {})
            paper_dict.update({
                "title": result.title,
                "authors": get_authors(result.authors),
                "summary": result.summary.replace("\n", " "),
                "arxiv_id": paper_id,
                "arxiv_url": ensure_https(f"{arxiv_url}abs/{paper_id}"),
                "pdf_url": ensure_https(f"{arxiv_url}pdf/{paper_id}.pdf"),
                "updated": str(result.updated.date()) if result.updated else paper_dict.get("updated", ""),
                "published": str(result.published.date()) if result.published else paper_dict.get("published", ""),
                "primary_category": result.primary_category or "",
                "comments": result.comment or "",
            })
            papers[paper_id] = paper_dict
            data[topic] = papers
        if sleep_seconds:
            time.sleep(sleep_seconds)

    with open(filename, "w") as f:
        json.dump(data, f)
def strip_md_bold(text: str) -> str:
    return text.replace("**", "")

def escape_html(text: str) -> str:
    return html.escape(text or "", quote=True)

def extract_first_url(text: str) -> str:
    if not text:
        return ""
    match = re.search(r"\((https?://[^)]+)\)", text)
    if match:
        return match.group(1)
    return ""

def ensure_https(url: str) -> str:
    if not url:
        return ""
    if url.startswith("http://arxiv.org/"):
        return url.replace("http://", "https://", 1)
    return url

def pretty_math(s: str) -> str:
    ret = ''
    match = re.search(r"\$.*\$", s)
    if match is None:
        return s
    math_start, math_end = match.span()
    space_trail = space_leading = ''
    prefix = s[:math_start]
    suffix = s[math_end:]
    if prefix and prefix[-1] != ' ' and '*' != prefix[-1]:
        space_trail = ' '
    if suffix and suffix[0] != ' ' and '*' != suffix[0]:
        space_leading = ' '
    ret += s[:math_start]
    ret += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
    ret += s[math_end:]
    return ret

def parse_paper_row(row: str):
    parts = row.strip().split("|")
    if len(parts) < 6:
        return "", "", "", "", ""
    date = strip_md_bold(parts[1].strip())
    title = strip_md_bold(parts[2].strip())
    authors = strip_md_bold(parts[3].strip())
    arxiv_id = strip_md_bold(parts[4].strip())
    code = strip_md_bold(parts[5].strip())
    return date, title, authors, arxiv_id, code

def paper_to_dict(paper_id: str, paper):
    if isinstance(paper, dict):
        paper["arxiv_url"] = ensure_https(paper.get("arxiv_url", ""))
        paper["pdf_url"] = ensure_https(paper.get("pdf_url", ""))
        return paper
    date, title, authors, arxiv_field, code_field = parse_paper_row(str(paper))
    arxiv_link = extract_first_url(arxiv_field)
    if not arxiv_link:
        arxiv_link = f"{arxiv_url}abs/{paper_id}".replace("//abs", "/abs")
    arxiv_link = ensure_https(arxiv_link)
    pdf_url = arxiv_link.replace("/abs/", "/pdf/") + ".pdf" if arxiv_link else ""
    code_url = extract_first_url(code_field)
    return {
        "title": title,
        "authors": authors,
        "summary": "",
        "arxiv_id": paper_id,
        "arxiv_url": arxiv_link,
        "pdf_url": pdf_url,
        "code_url": code_url,
        "updated": date,
        "published": "",
        "primary_category": "",
        "comments": "",
    }

def parse_paper_date(row: str):
    date, _, _, _, _ = parse_paper_row(row)
    try:
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None

def strip_arxiv_version(arxiv_id: str) -> str:
    return re.sub(r"v\\d+$", "", arxiv_id or "")

def fetch_arxiv_metadata(id_list):
    if arxiv is None:
        raise RuntimeError("Missing dependency: install the 'arxiv' package to fetch papers.")
    client = make_arxiv_client()
    search = arxiv.Search(id_list=id_list)
    results = {}
    for result in client.results(search):
        short_id = strip_arxiv_version(result.get_short_id())
        results[short_id] = result
    return results

def get_paper_date(paper):
    if isinstance(paper, dict):
        date_str = paper.get("updated") or paper.get("published") or ""
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return None
    return parse_paper_date(str(paper))

def slugify_topic(topic: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    return slug

def normalize_topics(data: dict, topic_merge: dict, topic_drop: list, allowed_topics: list):
    normalized = {}
    drop_set = set(topic_drop or [])
    for topic, papers in data.items():
        if topic in drop_set:
            continue
        target = topic_merge.get(topic, topic) if topic_merge else topic
        if allowed_topics and target not in allowed_topics:
            continue
        normalized.setdefault(target, {}).update(papers)
    if allowed_topics:
        ordered = {}
        for topic in allowed_topics:
            ordered[topic] = normalized.get(topic, {})
        return ordered
    return normalized

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def get_latest_date(papers: dict):
    latest = None
    for row in papers.values():
        if row is None:
            continue
        parsed = get_paper_date(row)
        if parsed and (latest is None or parsed > latest):
            latest = parsed
    return latest

def topic_link(topic: str, topics_dir: str, link_ext: str):
    slug = slugify_topic(topic)
    path = os.path.join(topics_dir, f"{slug}{link_ext}")
    return path.replace("\\", "/")

TOPIC_EMOJI = {
    "Point Cloud Registration": "🧭",
    "Image Matching": "🧩",
    "SLAM": "🛰️",
    "3D Reconstruction": "🧱",
    "Visual Localization": "🗺️",
    "NeRF": "🌫️",
    "Gaussian Splatting": "✨",
    "World Model": "🌍",
    "Flow Matching": "🌊",
}

TOPIC_ACCENTS = {
    "Point Cloud Registration": "#2563eb",
    "Image Matching": "#059669",
    "SLAM": "#d97706",
    "3D Reconstruction": "#7c3aed",
    "Visual Localization": "#0891b2",
    "NeRF": "#16a34a",
    "Gaussian Splatting": "#db2777",
    "World Model": "#9333ea",
    "Flow Matching": "#e11d48",
}

ICON_SVG = (
    "<svg viewBox=\"0 0 24 24\" aria-hidden=\"true\" focusable=\"false\">"
    "<path d=\"M12 2.5 20.5 7v10L12 21.5 3.5 17V7z\" fill=\"currentColor\" opacity=\"0.25\"/>"
    "<path d=\"M12 4.2 18.7 8v8L12 19.8 5.3 16V8z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.5\"/>"
    "</svg>"
)

def write_index_page(data: dict,
                     md_filename: str,
                     topics_dir: str,
                     link_ext: str,
                     usage_link: str,
                     show_badge: bool,
                     to_web: bool,
                     pages_url: str = "",
                     repo_url: str = ""):
    date_now = str(datetime.date.today()).replace("-", ".")
    total_papers = sum(len(papers) for papers in data.values() if papers)
    with open(md_filename, "w+") as f:
        if to_web:
            f.write("---\nlayout: default\n---\n\n")
            f.write("<section class=\"hero\">\n")
            f.write("  <div class=\"hero-content\">\n")
            f.write("    <p class=\"eyebrow\">3D Vision arXiv Daily</p>\n")
            f.write("    <h1>Daily radar for 3D vision papers</h1>\n")
            f.write("    <p class=\"hero-lede\">Track fresh papers across the 3D stack with curated topics, clean summaries, and code links.</p>\n")
            f.write("    <div class=\"hero-actions\">\n")
            f.write("      <a class=\"btn primary\" href=\"#topics\">Explore topics</a>\n")
            if repo_url:
                f.write(f"      <a class=\"btn ghost\" href=\"{repo_url}\">GitHub repo</a>\n")
            f.write("    </div>\n")
            f.write("  </div>\n")
            f.write("  <div class=\"hero-panel\">\n")
            f.write(f"    <div class=\"stat\"><span>Updated</span><strong>{date_now}</strong></div>\n")
            f.write(f"    <div class=\"stat\"><span>Topics</span><strong>{len(data)}</strong></div>\n")
            f.write(f"    <div class=\"stat\"><span>Total papers</span><strong>{total_papers}</strong></div>\n")
            f.write("  </div>\n")
            f.write("</section>\n\n")

            f.write("<section id=\"topics\" class=\"section\">\n")
            f.write("  <div class=\"section-head\">\n")
            f.write("    <h2>Topics</h2>\n")
            f.write("    <p>Pick a domain to dive into the latest papers and code.</p>\n")
            f.write("  </div>\n")
            f.write("  <div class=\"topic-grid\">\n")
            for topic, papers in data.items():
                latest = get_latest_date(papers)
                latest_str = latest.isoformat() if latest else "-"
                count = len(papers) if papers else 0
                link = topic_link(topic, topics_dir, link_ext)
                accent = TOPIC_ACCENTS.get(topic, "#28d8ff")
                f.write(f"    <a class=\"topic-card\" href=\"{link}\" style=\"--accent: {accent};\">\n")
                f.write(f"      <span class=\"topic-icon\">{ICON_SVG}</span>\n")
                f.write(f"      <h3>{escape_html(topic)}</h3>\n")
                f.write(f"      <p>Latest: {latest_str} · Papers: {count}</p>\n")
                f.write("      <span class=\"topic-cta\">View papers →</span>\n")
                f.write("    </a>\n")
            f.write("  </div>\n")
            f.write("</section>\n")
            return

        if show_badge:
            f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
            f.write(f"[![Forks][forks-shield]][forks-url]\n")
            f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
            f.write(f"[![Issues][issues-shield]][issues-url]\n\n")
        f.write("# 3D Vision arXiv Daily 🚀\n\n")
        if pages_url:
            f.write(f"> 🌐 Start here: **[GitHub Pages]({pages_url})**\n")
        f.write(f"> Updated on {date_now}\n")
        f.write(f"> Topics: {len(data)} | Total papers: {total_papers}\n")
        f.write(f"> Usage instructions: [here]({usage_link})\n")
        f.write("> This page is modified from [here](https://github.com/Vincentqyw/cv-arxiv-daily)\n\n")

        f.write("## Quick Access\n\n")
        if pages_url:
            f.write(f"- 🌌 Live reading: [GitHub Pages]({pages_url})\n")
        if repo_url:
            f.write(f"- 🧑‍💻 Source code: [Repository]({repo_url})\n")
        f.write(f"- 📘 Usage: [Setup guide]({usage_link})\n")
        f.write("\n")

        f.write("## Topics Navigator\n\n")
        f.write("| | Topic | Latest Update | Papers | Link |\n")
        f.write("|---|---|---|---|---|\n")
        for topic, papers in data.items():
            latest = get_latest_date(papers)
            latest_str = latest.isoformat() if latest else "-"
            count = len(papers) if papers else 0
            link = topic_link(topic, topics_dir, link_ext)
            emoji = TOPIC_EMOJI.get(topic, "📌")
            f.write(f"| {emoji} | {topic} | {latest_str} | {count} | [{topic}]({link}) |\n")
        f.write("\n")

        f.write("## How It Works\n\n")
        f.write("- Configure search keywords in `config.yaml`.\n")
        f.write("- Run `daily_arxiv.py` (or GitHub Actions) to refresh JSON and Markdown outputs.\n")
        f.write("- Browse the topic pages for full paper lists.\n\n")

        if show_badge:
            f.write((f"[contributors-shield]: https://img.shields.io/github/"
                     f"contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[contributors-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/graphs/contributors\n"))
            f.write((f"[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[forks-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/network/members\n"))
            f.write((f"[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[stars-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/stargazers\n"))
            f.write((f"[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[issues-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/issues\n\n"))

def _first_author_display(authors: str) -> str:
    if not authors:
        return ""
    first = authors.split(",")[0].strip()
    return f"{first} et al." if "," in authors else first

def write_topic_page(topic: str, papers: dict, md_path: str, to_web: bool,
                     all_topics: dict = None):
    date_now = str(datetime.date.today()).replace("-", ".")
    with open(md_path, "w+") as f:
        if to_web:
            f.write("---\nlayout: reader\n")
            f.write(f"title: {topic}\n---\n\n")

            # --- reader layout ---
            f.write("<div class=\"reader\">\n")

            # header
            f.write("  <header class=\"reader-header\">\n")
            f.write("    <a class=\"brand\" href=\"../index.html\">\n")
            f.write("      <span class=\"brand-mark\"></span>\n")
            f.write("      <span>3D Vision arXiv Daily</span>\n")
            f.write("    </a>\n")
            f.write(f"    <span class=\"reader-title\">{escape_html(topic)}")
            f.write(f" <span class=\"reader-count\">{len(papers)} papers</span></span>\n")
            f.write("    <nav class=\"reader-nav\">\n")
            f.write("      <a href=\"../index.html\">Dashboard</a>\n")
            f.write("    </nav>\n")
            f.write("  </header>\n")

            # sidebar
            f.write("  <nav class=\"reader-sidebar\">\n")
            f.write("    <div class=\"sidebar-title\">Topics</div>\n")
            topics_for_sidebar = all_topics if all_topics else {topic: papers}
            for t, t_papers in topics_for_sidebar.items():
                slug = slugify_topic(t)
                active = " active" if t == topic else ""
                count = len(t_papers) if t_papers else 0
                f.write(f"    <a class=\"sidebar-link{active}\" href=\"{slug}.html\">")
                f.write(f"{escape_html(t)} <span class=\"sidebar-count\">{count}</span></a>\n")
            f.write("  </nav>\n")

            # paper list
            f.write("  <section class=\"reader-list\">\n")
            f.write(f"    <div class=\"list-header\"><h2>{escape_html(topic)}</h2>")
            f.write(f"<span>{len(papers)} papers</span></div>\n")
            f.write("    <div class=\"list-items\">\n")
            sorted_items = sort_papers_by_date(papers)
            for paper_id, paper in sorted_items:
                paper_data = paper_to_dict(paper_id, paper)
                title = escape_html(paper_data.get("title", "Untitled"))
                authors_full = paper_data.get("authors", "")
                first_author = escape_html(_first_author_display(authors_full))
                updated = paper_data.get("updated", "")
                f.write(f"      <div class=\"list-item\" data-id=\"{escape_html(paper_id)}\">\n")
                f.write(f"        <div class=\"list-item-title\">{title}</div>\n")
                meta_parts = []
                if first_author:
                    meta_parts.append(first_author)
                if updated:
                    meta_parts.append(updated)
                f.write(f"        <div class=\"list-item-meta\">{' · '.join(meta_parts)}</div>\n")
                f.write("      </div>\n")
            f.write("    </div>\n")
            f.write("  </section>\n")

            # detail panel (populated by JS)
            f.write("  <section class=\"reader-detail\" id=\"reader-detail\">\n")
            f.write("    <div class=\"detail-empty\">Select a paper to read</div>\n")
            f.write("  </section>\n")

            f.write("</div>\n\n")

            # JSON data blob for JS
            papers_json = {}
            for paper_id, paper in sorted_items:
                pd = paper_to_dict(paper_id, paper)
                summary = (pd.get("summary", "") or "").strip()
                if not summary:
                    summary = "Abstract unavailable. It will appear after the next refresh."
                papers_json[paper_id] = {
                    "title": pd.get("title", ""),
                    "authors": pd.get("authors", ""),
                    "summary": summary,
                    "arxiv_url": ensure_https(pd.get("arxiv_url", "")),
                    "pdf_url": ensure_https(pd.get("pdf_url", "")),
                    "code_url": pd.get("code_url", ""),
                    "updated": pd.get("updated", ""),
                    "comments": pd.get("comments", ""),
                }
            f.write("<script id=\"papers-data\" type=\"application/json\">\n")
            f.write(json.dumps(papers_json, ensure_ascii=False))
            f.write("\n</script>\n")
            return

        f.write(f"# {topic}\n\n")
        f.write(f"> Updated on {date_now}\n\n")
        f.write("| Publish Date | Title | Authors | PDF | Code |\n")
        f.write("|:---------|:-----------------------|:---------|:------|:------|\n")
        sorted_papers = sort_papers(papers)
        for _, row in sorted_papers.items():
            if row is not None:
                f.write(pretty_math(str(row)))
        f.write("\n")

def write_topic_pages(data: dict, topics_dir: str, to_web: bool):
    ensure_dir(topics_dir)
    for topic, papers in data.items():
        slug = slugify_topic(topic)
        md_path = os.path.join(topics_dir, f"{slug}.md")
        write_topic_page(topic, papers, md_path, to_web, all_topics=data)

def get_code_link(qword:str) -> str:
    """
    This short function was auto-generated by ChatGPT. 
    I only renamed some params and added some comments.
    @param qword: query string, eg. arxiv ids and paper titles
    @return paper_code in github: string, if not found, return None
    """
    try:
        # query = f"arxiv:{arxiv_id}"
        query = f"{qword}"
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc"
        }
        r = requests.get(github_url, params=params)
        results = r.json()
        code_link = None
        if "total_count" in results and results["total_count"] > 0:
            code_link = results["items"][0]["html_url"]
        return code_link
    except Exception as e:
        logging.debug(f"GitHub search failed for {qword}: {e}")
        return None
  
def get_daily_papers(topic, query="slam", max_results=2, client=None):
    """
    @param topic: str
    @param query: str
    @param client: arxiv.Client (optional, shared across calls to respect rate limits)
    @return paper_with_code: dict
    """
    if arxiv is None:
        raise RuntimeError("Missing dependency: install the 'arxiv' package to fetch papers.")
    # output
    content = dict()
    content_to_web = dict()
    content_to_wechat = dict()
    if client is None:
        client = make_arxiv_client()
    search = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    for result in client.results(search):

        paper_id            = result.get_short_id()
        paper_title         = result.title
        paper_url           = result.entry_id
        paper_abstract      = result.summary.replace("\n"," ")
        paper_authors       = get_authors(result.authors)
        paper_first_author  = get_authors(result.authors,first_author = True)
        primary_category    = result.primary_category
        publish_time        = result.published.date()
        update_time         = result.updated.date()
        comments            = result.comment

        logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author}")

        # eg: 2108.09112v1 -> 2108.09112
        ver_pos = paper_id.find('v')
        if ver_pos == -1:
            paper_key = paper_id
        else:
            paper_key = paper_id[0:ver_pos]    
        paper_url = arxiv_url + 'abs/' + paper_key
        
        # Try to find code link from GitHub search
        repo_url = get_code_link(paper_title)
        if repo_url is None:
            repo_url = get_code_link(paper_key)
        
        if repo_url is not None:
            content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|**[link]({})**|\n".format(
                   update_time, paper_title, paper_first_author, paper_key, paper_url, repo_url)
            content_to_wechat[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({}), Code: **[{}]({})**".format(
                   update_time, paper_title, paper_first_author, paper_url, paper_url, repo_url, repo_url)
        else:
            content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|null|\n".format(
                   update_time, paper_title, paper_first_author, paper_key, paper_url)
            content_to_wechat[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
                   update_time, paper_title, paper_first_author, paper_url, paper_url)

        content_to_web[paper_key] = {
            "title": paper_title,
            "authors": paper_authors,
            "summary": paper_abstract,
            "arxiv_id": paper_key,
            "arxiv_url": paper_url,
            "pdf_url": f"{arxiv_url}pdf/{paper_key}.pdf",
            "code_url": repo_url or "",
            "updated": str(update_time),
            "published": str(publish_time),
            "primary_category": primary_category,
            "comments": comments or "",
        }

        # TODO: select useful comments
        comments = None
        if comments != None:
            content_to_wechat[paper_key] += f", {comments}\n"
        else:
            content_to_wechat[paper_key] += f"\n"

    data = {topic: content}
    data_web = {topic: content_to_web}
    data_wechat = {topic: content_to_wechat}
    return data, data_web, data_wechat 

def update_paper_links(filename, topic_merge=None, topic_drop=None, allowed_topics=None):
    '''
    weekly update paper links in json file 
    '''
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)
            
        json_data = normalize_topics(
            m.copy(),
            topic_merge or {},
            topic_drop or [],
            allowed_topics or []
        )

        for keywords, v in json_data.items():
            logging.info(f'keywords = {keywords}')
            for paper_id, contents in v.items():
                if isinstance(contents, dict):
                    code_url = contents.get("code_url") or ""
                    if code_url:
                        continue
                    repo_url = get_code_link(contents.get("title", ""))
                    if repo_url is None:
                        repo_url = get_code_link(paper_id)
                    if repo_url is not None:
                        contents["code_url"] = repo_url
                        json_data[keywords][paper_id] = contents
                    continue

                contents = str(contents)

                update_time, paper_title, paper_first_author, paper_url, code_url = parse_paper_row(contents)
                paper_url = re.sub(r'v\d+', '', paper_url)

                contents = "|{}|{}|{}|{}|{}|\n".format(update_time, paper_title, paper_first_author, paper_url, code_url)
                json_data[keywords][paper_id] = str(contents)
                logging.info(f'paper_id = {paper_id}, contents = {contents}')

                valid_link = False if '|null|' in contents else True
                if valid_link:
                    continue
                # Try to find code link from GitHub search
                repo_url = get_code_link(paper_title)
                if repo_url is None:
                    repo_url = get_code_link(paper_id)
                if repo_url is not None:
                    new_cont = contents.replace('|null|', f'|**[link]({repo_url})**|')
                    logging.info(f'ID = {paper_id}, contents = {new_cont}')
                    json_data[keywords][paper_id] = str(new_cont)
        # dump to json file
        with open(filename,"w") as f:
            json.dump(json_data,f)

def update_json_file(filename, data_dict, topic_merge=None, topic_drop=None, allowed_topics=None):
    '''
    daily update json file using data_dict
    '''
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)
            
    json_data = normalize_topics(
        m.copy(),
        topic_merge or {},
        topic_drop or [],
        allowed_topics or []
    )
    
    # update papers in each keywords
    for data in data_dict:
        for keyword in data.keys():
            papers = data[keyword]

            if keyword in json_data.keys():
                json_data[keyword].update(papers)
            else:
                json_data[keyword] = papers
    json_data = normalize_topics(
        json_data,
        topic_merge or {},
        topic_drop or [],
        allowed_topics or []
    )

    with open(filename,"w") as f:
        json.dump(json_data,f)
    
def json_to_md(filename, md_filename,
               task = '',
               to_web = False,
               use_title = True,
               use_tc = True,
               show_badge = True,
               use_b2t = True,
               topic_merge = None,
               topic_drop = None,
               allowed_topics = None):
    """
    @param filename: str
    @param md_filename: str
    @return None
    """
    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-','.')
    
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)
    data = normalize_topics(
        data,
        topic_merge or {},
        topic_drop or [],
        allowed_topics or []
    )

    # clean README.md if daily already exist else create it
    with open(md_filename,"w+") as f:
        pass

    # write data into README.md
    with open(md_filename,"a+") as f:

        if (use_title == True) and (to_web == True):
            f.write("---\n" + "layout: default\n" + "---\n\n")
        
        if show_badge == True:
            f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
            f.write(f"[![Forks][forks-shield]][forks-url]\n")
            f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
            f.write(f"[![Issues][issues-shield]][issues-url]\n\n")    
                
        if use_title == True:
            #f.write(("<p align="center"><h1 align="center"><br><ins>CV-ARXIV-DAILY"
            #         "</ins><br>Automatically Update CV Papers Daily</h1></p>\n"))
            f.write("## Updated on " + DateNow + "\n")
        else:
            f.write("> Updated on " + DateNow + "\n")

        # TODO: add usage
        f.write("> Usage instructions: [here](./docs/README.md#usage)\n\n")
        f.write("> This page is modified from [here](https://github.com/Vincentqyw/cv-arxiv-daily)\n\n")

        #Add: table of contents
        if use_tc == True:
            f.write("<details>\n")
            f.write("  <summary>Table of Contents</summary>\n")
            f.write("  <ol>\n")
            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                kw = keyword.replace(' ','-')      
                f.write(f"    <li><a href=#{kw.lower()}>{keyword}</a></li>\n")
            f.write("  </ol>\n")
            f.write("</details>\n\n")
        
        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            # the head of each part
            f.write(f"## {keyword}\n\n")

            if use_title == True :
                if to_web == False:
                    f.write("|Publish Date|Title|Authors|PDF|Code|\n" + "|---|---|---|---|---|\n")
                else:
                    f.write("| Publish Date | Title | Authors | PDF | Code |\n")
                    f.write("|:---------|:-----------------------|:---------|:------|:------|\n")

            # sort papers by date
            day_content = sort_papers(day_content)
        
            for _,v in day_content.items():
                if v is not None:
                    f.write(pretty_math(v)) # make latex pretty

            f.write(f"\n")
            
            #Add: back to top
            if use_b2t:
                top_info = f"#Updated on {DateNow}"
                top_info = top_info.replace(' ','-').replace('.','')
                f.write(f"<p align=right>(<a href={top_info.lower()}>back to top</a>)</p>\n\n")
            
        if show_badge == True:
            # we don't like long string, break it!
            f.write((f"[contributors-shield]: https://img.shields.io/github/"
                     f"contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[contributors-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/graphs/contributors\n"))
            f.write((f"[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[forks-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/network/members\n"))
            f.write((f"[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[stars-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/stargazers\n"))
            f.write((f"[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[issues-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/issues\n\n"))
                
    logging.info(f"{task} finished")        

def demo(**config):
    # TODO: use config
    data_collector = []
    data_collector_web = []
    data_collector_wechat = []
    
    keywords = config['kv']
    max_results = config['max_results']
    publish_readme = config['publish_readme']
    publish_gitpage = config['publish_gitpage']
    publish_wechat = config['publish_wechat']
    show_badge = config['show_badge']
    topic_merge = config.get('topic_merge', {})
    topic_drop = config.get('topic_drop', [])
    allowed_topics = list(config['keywords'].keys())
    readme_topics_dir = config.get('md_readme_topics_dir', './topics')
    gitpage_topics_dir = config.get('md_gitpage_topics_dir', './docs/topics')
    backfill_abstracts = config.get('backfill_abstracts', False)
    backfill_max_papers = config.get('backfill_max_papers', 0)
    backfill_chunk_size = config.get('backfill_chunk_size', 40)
    backfill_sleep_seconds = config.get('backfill_sleep_seconds', 1.0)

    b_update = config['update_paper_links']
    logging.info(f'Update Paper Link = {b_update}')
    if config['update_paper_links'] == False:
        logging.info(f"GET daily papers begin")
        shared_client = make_arxiv_client() if arxiv else None
        for topic, keyword in keywords.items():
            logging.info(f"Keyword: {topic}")
            data, data_web, data_wechat = get_daily_papers(topic, query = keyword,
                                                          max_results = max_results,
                                                          client = shared_client)
            data_collector.append(data)
            data_collector_web.append(data_web)
            data_collector_wechat.append(data_wechat)
            print("\n")
            time.sleep(5)
        logging.info(f"GET daily papers end")

    # 1. update README.md file
    if publish_readme:
        json_file = config['json_readme_path']
        md_file   = config['md_readme_path']
        # update paper links
        if config['update_paper_links']:
            update_paper_links(
                json_file,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics
            )
        else:    
            # update json data
            update_json_file(
                json_file,
                data_collector,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics
            )
        with open(json_file, "r") as f:
            content = f.read()
            data = json.loads(content) if content else {}
        data = normalize_topics(data, topic_merge, topic_drop, allowed_topics)
        readme_topics_link_dir = os.path.relpath(
            readme_topics_dir,
            start=os.path.dirname(md_file) or "."
        )
        write_index_page(
            data,
            md_file,
            readme_topics_link_dir,
            link_ext=".md",
            usage_link="./docs/README.md#usage",
            show_badge=show_badge,
            to_web=False,
            pages_url=config.get("pages_url", ""),
            repo_url=config.get("repo_url", "")
        )
        write_topic_pages(data, readme_topics_dir, to_web=False)

    # 2. update docs/index.md file (to gitpage)
    if publish_gitpage:
        json_file = config['json_gitpage_path']
        md_file   = config['md_gitpage_path']
        # TODO: duplicated update paper links!!!
        if config['update_paper_links']:
            update_paper_links(
                json_file,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics
            )
        else:    
            update_json_file(
                json_file,
                data_collector_web,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics
            )
        if backfill_abstracts:
            backfill_web_abstracts(
                json_file,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics,
                max_total=backfill_max_papers,
                chunk_size=backfill_chunk_size,
                sleep_seconds=backfill_sleep_seconds
            )
        with open(json_file, "r") as f:
            content = f.read()
            data = json.loads(content) if content else {}
        data = normalize_topics(data, topic_merge, topic_drop, allowed_topics)
        gitpage_topics_link_dir = os.path.relpath(
            gitpage_topics_dir,
            start=os.path.dirname(md_file) or "."
        )
        write_index_page(
            data,
            md_file,
            gitpage_topics_link_dir,
            link_ext=".html",
            usage_link="README.html#usage",
            show_badge=show_badge,
            to_web=True,
            pages_url=config.get("pages_url", ""),
            repo_url=config.get("repo_url", "")
        )
        write_topic_pages(data, gitpage_topics_dir, to_web=True)

    # 3. Update docs/wechat.md file
    if publish_wechat:
        json_file = config['json_wechat_path']
        md_file   = config['md_wechat_path']
        # TODO: duplicated update paper links!!!
        if config['update_paper_links']:
            update_paper_links(
                json_file,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics
            )
        else:    
            update_json_file(
                json_file,
                data_collector_wechat,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics
            )
        json_to_md(
            json_file,
            md_file,
            task='Update Wechat',
            to_web=False,
            use_title=False,
            show_badge=show_badge,
            topic_merge=topic_merge,
            topic_drop=topic_drop,
            allowed_topics=allowed_topics
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path',type=str, default='config.yaml',
                            help='configuration file path')
    parser.add_argument('--update_paper_links', default=False,
                        action="store_true",help='whether to update paper links etc.')                        
    args = parser.parse_args()
    config = load_config(args.config_path)
    config = {**config, 'update_paper_links':args.update_paper_links}
    demo(**config)
