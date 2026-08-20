window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"], ["\\$", "\\$"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*",
    processHtmlClass: "arithmatex"
  },
  // Force mathjax to wait for config to be loaded before processing math
  startup: {
    ready: () => {
      MathJax.startup.defaultReady();
    }
  }
};

// Trigger MathJax when changing pages via instant loading
document$.subscribe(() => {
  if (typeof MathJax !== "undefined" && typeof MathJax.typesetPromise === "function") {
    MathJax.typesetPromise();
  }
});