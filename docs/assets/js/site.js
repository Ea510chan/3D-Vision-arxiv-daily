(() => {
  const loadPreview = (preview) => {
    const pdfUrl = preview.dataset.pdf;
    if (!pdfUrl) return;

    const placeholder = preview.querySelector(".preview-placeholder");
    const viewerUrl =
      "https://docs.google.com/gview?url=" +
      encodeURIComponent(pdfUrl) +
      "&embedded=true";

    if (placeholder) placeholder.textContent = "Loading preview…";

    const iframe = document.createElement("iframe");
    iframe.className = "preview-frame";
    iframe.loading = "lazy";
    iframe.title = "Paper preview";
    iframe.src = viewerUrl;

    // Google Docs viewer can be slow; give it a timeout
    const timeout = setTimeout(() => {
      if (!iframe.classList.contains("is-ready")) {
        if (placeholder) {
          placeholder.innerHTML =
            'Preview timed out — <a href="' +
            pdfUrl +
            '" target="_blank" rel="noopener">open PDF directly</a>';
        }
        iframe.remove();
      }
    }, 15000);

    iframe.addEventListener("load", () => {
      clearTimeout(timeout);
      iframe.classList.add("is-ready");
      if (placeholder) placeholder.style.display = "none";
    });

    preview.appendChild(iframe);
  };

  document.addEventListener(
    "toggle",
    (event) => {
      const details = event.target;
      if (!(details instanceof HTMLDetailsElement) || !details.open) return;
      const preview = details.querySelector(".paper-preview[data-pdf]");
      if (!preview || preview.dataset.loaded === "true") return;
      preview.dataset.loaded = "true";
      loadPreview(preview);
    },
    true
  );
})();
