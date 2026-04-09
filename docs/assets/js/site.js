(() => {
  // Convert arxiv PDF URL to ar5iv HTML preview URL
  // e.g. https://arxiv.org/pdf/2603.21785.pdf -> https://ar5iv.labs.arxiv.org/html/2603.21785
  const toAr5ivUrl = (pdfUrl) => {
    const match = pdfUrl.match(/arxiv\.org\/pdf\/([^/.]+(?:\.\d+)?)/);
    if (!match) return null;
    return `https://ar5iv.labs.arxiv.org/html/${match[1]}`;
  };

  const loadPreview = (preview) => {
    const pdfUrl = preview.dataset.pdf;
    if (!pdfUrl) return;

    const placeholder = preview.querySelector(".preview-placeholder");
    const ar5ivUrl = toAr5ivUrl(pdfUrl);

    if (!ar5ivUrl) {
      if (placeholder) placeholder.textContent = "Preview not available.";
      return;
    }

    if (placeholder) placeholder.textContent = "Loading paper preview…";

    const iframe = document.createElement("iframe");
    iframe.className = "preview-frame";
    iframe.sandbox = "allow-scripts allow-same-origin";
    iframe.loading = "lazy";
    iframe.title = "Paper preview";
    iframe.src = ar5ivUrl;

    iframe.addEventListener("load", () => {
      iframe.classList.add("is-ready");
      if (placeholder) placeholder.style.display = "none";
    });

    iframe.addEventListener("error", () => {
      if (placeholder) {
        placeholder.textContent = "Preview unavailable — ";
        const link = document.createElement("a");
        link.href = pdfUrl;
        link.textContent = "open PDF directly";
        link.target = "_blank";
        link.rel = "noopener";
        placeholder.appendChild(link);
      }
    });

    preview.appendChild(iframe);
  };

  // Lazy-load on expand
  document.addEventListener("toggle", (event) => {
    const details = event.target;
    if (!(details instanceof HTMLDetailsElement) || !details.open) return;
    const preview = details.querySelector(".paper-preview[data-pdf]");
    if (!preview || preview.dataset.loaded === "true") return;
    preview.dataset.loaded = "true";
    loadPreview(preview);
  }, true);
})();
