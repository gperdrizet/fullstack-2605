document.addEventListener('click', function (e) {
  var link = e.target.closest('a[href*="raw.githubusercontent.com"]');
  if (!link) return;
  e.preventDefault();
  var url = link.href;
  var filename = url.split('/').pop();
  fetch(url)
    .then(function (response) { return response.blob(); })
    .then(function (blob) {
      var blobUrl = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = blobUrl;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(blobUrl);
    });
});
