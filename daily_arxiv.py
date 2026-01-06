import os
import re
import json
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
arxiv_url = "http://arxiv.org/"

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
def strip_md_bold(text: str) -> str:
    return text.replace("**", "")

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
    date = parts[1].strip()
    title = parts[2].strip()
    authors = parts[3].strip()
    arxiv_id = parts[4].strip()
    code = parts[5].strip()
    return date, title, authors, arxiv_id, code

def parse_paper_date(row: str):
    date, _, _, _, _ = parse_paper_row(row)
    date = strip_md_bold(date)
    try:
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None

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
        parsed = parse_paper_date(str(row))
        if parsed and (latest is None or parsed > latest):
            latest = parsed
    return latest

def topic_link(topic: str, topics_dir: str, link_ext: str):
    slug = slugify_topic(topic)
    path = os.path.join(topics_dir, f"{slug}{link_ext}")
    return path.replace("\\", "/")

def write_index_page(data: dict,
                     md_filename: str,
                     topics_dir: str,
                     link_ext: str,
                     usage_link: str,
                     show_badge: bool,
                     to_web: bool):
    date_now = str(datetime.date.today()).replace("-", ".")
    total_papers = sum(len(papers) for papers in data.values() if papers)
    with open(md_filename, "w+") as f:
        if to_web:
            f.write("---\nlayout: default\n---\n\n")
        if show_badge and not to_web:
            f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
            f.write(f"[![Forks][forks-shield]][forks-url]\n")
            f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
            f.write(f"[![Issues][issues-shield]][issues-url]\n\n")
        f.write("# 3D Vision arXiv Daily\n\n")
        f.write(f"> Updated on {date_now}\n")
        f.write(f"> Topics: {len(data)} | Total papers: {total_papers}\n")
        f.write(f"> Usage instructions: [here]({usage_link})\n")
        f.write("> This page is modified from [here](https://github.com/Vincentqyw/cv-arxiv-daily)\n\n")
        f.write("## Topics\n\n")
        f.write("| Topic | Latest Update | Papers | Link |\n")
        f.write("|---|---|---|---|\n")
        for topic, papers in data.items():
            latest = get_latest_date(papers)
            latest_str = latest.isoformat() if latest else "-"
            count = len(papers) if papers else 0
            link = topic_link(topic, topics_dir, link_ext)
            f.write(f"| {topic} | {latest_str} | {count} | [{topic}]({link}) |\n")
        f.write("\n")
        f.write("## How It Works\n\n")
        f.write("- Configure search keywords in `config.yaml`.\n")
        f.write("- Run `daily_arxiv.py` (or GitHub Actions) to refresh JSON and Markdown outputs.\n")
        f.write("- Browse the topic pages for full paper lists.\n\n")
        if show_badge and not to_web:
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

def write_topic_page(topic: str, papers: dict, md_path: str, to_web: bool):
    date_now = str(datetime.date.today()).replace("-", ".")
    with open(md_path, "w+") as f:
        if to_web:
            f.write("---\nlayout: default\n")
            f.write(f"title: {topic}\n---\n\n")
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
        write_topic_page(topic, papers, md_path, to_web)

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
  
def get_daily_papers(topic,query="slam", max_results=2):
    """
    @param topic: str
    @param query: str
    @return paper_with_code: dict
    """
    if arxiv is None:
        raise RuntimeError("Missing dependency: install the 'arxiv' package to fetch papers.")
    # output 
    content = dict() 
    content_to_web = dict()
    client = arxiv.Client()
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
                   update_time,paper_title,paper_first_author,paper_key,paper_url,repo_url)
            content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({}), Code: **[{}]({})**".format(
                   update_time,paper_title,paper_first_author,paper_url,paper_url,repo_url,repo_url)
        else:
            content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|null|\n".format(
                   update_time,paper_title,paper_first_author,paper_key,paper_url)
            content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
                   update_time,paper_title,paper_first_author,paper_url,paper_url)

        # TODO: select useful comments
        comments = None
        if comments != None:
            content_to_web[paper_key] += f", {comments}\n"
        else:
            content_to_web[paper_key] += f"\n"

    data = {topic:content}
    data_web = {topic:content_to_web}
    return data,data_web 

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

        for keywords,v in json_data.items():
            logging.info(f'keywords = {keywords}')
            for paper_id,contents in v.items():
                contents = str(contents)

                update_time, paper_title, paper_first_author, paper_url, code_url = parse_paper_row(contents)
                paper_url = re.sub(r'v\d+', '', paper_url)

                contents = "|{}|{}|{}|{}|{}|\n".format(update_time,paper_title,paper_first_author,paper_url,code_url)
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
                    new_cont = contents.replace('|null|',f'|**[link]({repo_url})**|')
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
    data_collector_web= []
    
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

    b_update = config['update_paper_links']
    logging.info(f'Update Paper Link = {b_update}')
    if config['update_paper_links'] == False:
        logging.info(f"GET daily papers begin")
        for topic, keyword in keywords.items():
            logging.info(f"Keyword: {topic}")
            data, data_web = get_daily_papers(topic, query = keyword,
                                            max_results = max_results)
            data_collector.append(data)
            data_collector_web.append(data_web)
            print("\n")
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
            to_web=False
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
                data_collector,
                topic_merge=topic_merge,
                topic_drop=topic_drop,
                allowed_topics=allowed_topics
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
            to_web=True
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
                data_collector_web,
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
