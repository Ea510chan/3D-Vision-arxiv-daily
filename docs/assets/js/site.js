(() => {
  const loadPreview = (preview) => {
    const pdfUrl = preview.dataset.pdf;
    if (!pdfUrl) return;

    const placeholder = preview.querySelector(".preview-placeholder");
    if (placeholder) placeholder.textContent = "Loading preview…";

    const iframe = document.createElement("iframe");
    iframe.className = "preview-frame";
    iframe.loading = "lazy";
    iframe.title = "Paper PDF preview";
    iframe.src = pdfUrl;

    iframe.addEventListener("load", () => {
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
