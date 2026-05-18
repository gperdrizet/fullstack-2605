document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a.download-link').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var url = this.href;
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
  });
});
