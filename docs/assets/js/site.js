(() => {
  const dataEl = document.getElementById("papers-data");
  if (!dataEl) return;

  const papers = JSON.parse(dataEl.textContent);
  const detail = document.getElementById("reader-detail");
  const listItems = document.querySelectorAll(".list-item[data-id]");

  const escape = (s) => {
    const d = document.createElement("div");
    d.textContent = s || "";
    return d.innerHTML;
  };

  const toHtmlUrl = (pdfUrl) => {
    if (!pdfUrl) return "";
    const m = pdfUrl.match(/arxiv\.org\/pdf\/([^/.]+(?:\.\d+)?)/);
    return m ? `https://arxiv.org/html/${m[1]}` : "";
  };

  const selectPaper = (id) => {
    const p = papers[id];
    if (!p || !detail) return;

    listItems.forEach((el) => el.classList.toggle("active", el.dataset.id === id));

    let links = "";
    if (p.arxiv_url) links += `<a class="chip" href="${escape(p.arxiv_url)}" target="_blank" rel="noopener">arXiv</a>`;
    if (p.pdf_url) links += `<a class="chip" href="${escape(p.pdf_url)}" target="_blank" rel="noopener">PDF</a>`;
    if (p.code_url) links += `<a class="chip" href="${escape(p.code_url)}" target="_blank" rel="noopener">Code</a>`;
    if (!p.code_url) links += `<span class="chip ghost">Code: N/A</span>`;

    const comment = p.comments ? `<span class="detail-bar-comment">${escape(p.comments)}</span>` : "";

    const htmlUrl = toHtmlUrl(p.pdf_url);
    const viewer = htmlUrl
      ? `<div class="detail-viewer"><iframe src="${escape(htmlUrl)}" title="Paper HTML view"></iframe></div>`
      : `<div class="detail-empty">HTML version not available</div>`;

    detail.innerHTML =
      `<div class="detail-bar">` +
        `<div class="detail-bar-top">` +
          `<span class="detail-bar-title">${escape(p.title)}</span>` +
          `<div class="detail-bar-links">${links}</div>` +
        `</div>` +
        comment +
      `</div>` +
      viewer;
  };

  listItems.forEach((el) => {
    el.addEventListener("click", () => selectPaper(el.dataset.id));
  });

  if (listItems.length > 0) {
    selectPaper(listItems[0].dataset.id);
  }
})();
