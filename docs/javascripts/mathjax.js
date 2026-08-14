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
  }
};

// Trigger MathJax when changing pages via instant loading
document$.subscribe(() => {
  if (typeof MathJax !== "undefined" && typeof MathJax.typesetPromise === "function") {
    MathJax.typesetPromise();
  }
});