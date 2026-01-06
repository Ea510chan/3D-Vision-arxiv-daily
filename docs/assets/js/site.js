(() => {
  const previews = document.querySelectorAll(".paper-preview[data-pdf]");
  if (!previews.length) {
    return;
  }

  let pdfjsPromise = null;

  const loadPdfJs = () => {
    if (pdfjsPromise) {
      return pdfjsPromise;
    }
    pdfjsPromise = new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.2.67/build/pdf.min.js";
      script.onload = () => {
        if (!window.pdfjsLib) {
          reject(new Error("PDF.js failed to load."));
          return;
        }
        window.pdfjsLib.GlobalWorkerOptions.workerSrc =
          "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.2.67/build/pdf.worker.min.js";
        resolve(window.pdfjsLib);
      };
      script.onerror = () => reject(new Error("PDF.js script error."));
      document.head.appendChild(script);
    });
    return pdfjsPromise;
  };

  const renderPreview = async (preview) => {
    const pdfUrl = preview.dataset.pdf;
    if (!pdfUrl) {
      return;
    }
    const placeholder = preview.querySelector(".preview-placeholder");
    const canvas = preview.querySelector(".preview-canvas");
    if (!canvas) {
      return;
    }
    placeholder.textContent = "Rendering preview…";
    try {
      const pdfjsLib = await loadPdfJs();
      const loadingTask = pdfjsLib.getDocument(pdfUrl);
      const pdf = await loadingTask.promise;
      const page = await pdf.getPage(1);
      const viewport = page.getViewport({ scale: 1 });
      const maxWidth = 360;
      const scale = Math.min(1.4, maxWidth / viewport.width);
      const scaled = page.getViewport({ scale });
      canvas.width = scaled.width;
      canvas.height = scaled.height;
      const context = canvas.getContext("2d", { alpha: false });
      await page.render({ canvasContext: context, viewport: scaled }).promise;
      canvas.classList.add("is-ready");
      placeholder.textContent = "";
    } catch (error) {
      placeholder.textContent = "Preview unavailable for this paper.";
    }
  };

  document.addEventListener("toggle", (event) => {
    const details = event.target;
    if (!(details instanceof HTMLDetailsElement)) {
      return;
    }
    if (!details.open) {
      return;
    }
    const preview = details.querySelector(".paper-preview[data-pdf]");
    if (!preview || preview.dataset.loaded === "true") {
      return;
    }
    preview.dataset.loaded = "true";
    renderPreview(preview);
  });
})();
