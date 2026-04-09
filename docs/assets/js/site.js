(() => {
  const dataEl = document.getElementById("papers-data");
  if (!dataEl) return;

  const papers = JSON.parse(dataEl.textContent);
  const detail = document.getElementById("reader-detail");
  const listItems = document.querySelectorAll(".list-item[data-id]");

  const selectPaper = (id) => {
    const p = papers[id];
    if (!p || !detail) return;

    // highlight active list item
    listItems.forEach((el) => el.classList.toggle("active", el.dataset.id === id));

    const escape = (s) => {
      const d = document.createElement("div");
      d.textContent = s || "";
      return d.innerHTML;
    };

    let linksHtml = "";
    if (p.arxiv_url) linksHtml += `<a class="chip" href="${escape(p.arxiv_url)}" target="_blank" rel="noopener">arXiv</a>`;
    if (p.pdf_url) linksHtml += `<a class="chip" href="${escape(p.pdf_url)}" target="_blank" rel="noopener">PDF</a>`;
    if (p.code_url) linksHtml += `<a class="chip" href="${escape(p.code_url)}" target="_blank" rel="noopener">Code</a>`;
    if (!p.code_url) linksHtml += `<span class="chip ghost">Code: N/A</span>`;

    const pdfIframe = p.pdf_url
      ? `<div class="detail-pdf"><iframe src="${escape(p.pdf_url)}" title="PDF preview" loading="lazy"></iframe></div>`
      : "";

    detail.innerHTML = `
      <div class="detail-content">
        <div class="detail-header">
          <div class="detail-title">${escape(p.title)}</div>
          <div class="detail-authors">${escape(p.authors)}</div>
          <div class="detail-date">Updated ${escape(p.updated)}</div>
          <div class="detail-links">${linksHtml}</div>
        </div>
        <div class="detail-abstract">
          <div class="detail-abstract-label">Abstract</div>
          <p>${escape(p.summary || "Abstract unavailable.")}</p>
        </div>
        ${pdfIframe}
      </div>`;
  };

  // click handlers for paper list items
  listItems.forEach((el) => {
    el.addEventListener("click", () => selectPaper(el.dataset.id));
  });

  // select first paper by default
  if (listItems.length > 0) {
    selectPaper(listItems[0].dataset.id);
  }
})();
