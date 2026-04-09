(() => {
  /* ─── Resizable columns ─── */
  const reader = document.querySelector(".reader");
  if (reader) {
    const handles = reader.querySelectorAll(".col-resize");
    handles.forEach((handle, idx) => {
      let startX, startWidths;

      const onMouseMove = (e) => {
        const dx = e.clientX - startX;
        // cols: [sidebar, handle, list, handle, detail]
        if (idx === 0) {
          const sidebar = Math.max(120, Math.min(360, startWidths[0] + dx));
          reader.style.gridTemplateColumns = `${sidebar}px 5px ${startWidths[2]}px 5px 1fr`;
        } else {
          const list = Math.max(200, Math.min(600, startWidths[2] + dx));
          reader.style.gridTemplateColumns = `${startWidths[0]}px 5px ${list}px 5px 1fr`;
        }
      };

      const onMouseUp = () => {
        handle.classList.remove("dragging");
        document.removeEventListener("mousemove", onMouseMove);
        document.removeEventListener("mouseup", onMouseUp);
        // re-enable iframe pointer events
        reader.querySelectorAll("iframe").forEach((f) => (f.style.pointerEvents = ""));
      };

      handle.addEventListener("mousedown", (e) => {
        e.preventDefault();
        handle.classList.add("dragging");
        startX = e.clientX;
        const cols = getComputedStyle(reader).gridTemplateColumns.split(/\s+/);
        startWidths = cols.map((c) => parseFloat(c));
        // disable iframe pointer events during drag so mousemove works
        reader.querySelectorAll("iframe").forEach((f) => (f.style.pointerEvents = "none"));
        document.addEventListener("mousemove", onMouseMove);
        document.addEventListener("mouseup", onMouseUp);
      });
    });
  }

  /* ─── Paper selection ─── */
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

    const htmlUrl = toHtmlUrl(p.pdf_url);
    const viewer = htmlUrl
      ? `<div class="detail-viewer"><iframe src="${escape(htmlUrl)}" title="Paper HTML view"></iframe></div>`
      : `<div class="detail-empty">HTML version not available</div>`;

    detail.innerHTML =
      `<div class="detail-bar">` +
        `<span class="detail-bar-title">${escape(p.title)}</span>` +
        `<div class="detail-bar-links">${links}</div>` +
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
