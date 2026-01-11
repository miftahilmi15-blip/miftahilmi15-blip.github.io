document.addEventListener("DOMContentLoaded", function () {

  let currentPage = 1;
  const totalPages = 604;

  const surahContent = document.getElementById("surahContent");
  const pageNumber = document.getElementById("pageNumber");

  function renderPage() {
    surahContent.innerHTML = `
      <img 
        src="mushaf/page-${currentPage}.svg" 
        alt="Halaman ${currentPage}"
        style="width:100%; max-width:600px;"
      >
    `;
    pageNumber.textContent = currentPage;
  }

  window.nextPage = function () {
    if (currentPage < totalPages) {
      currentPage++;
      renderPage();
    }
  };

  window.prevPage = function () {
    if (currentPage > 1) {
      currentPage--;
      renderPage();
    }
  };

  window.toggleDark = function () {
    document.body.classList.toggle("dark");
  };

  renderPage();
});

function toggleDark() {
  document.body.classList.toggle("dark");
}

// render pertama kali
renderPage();
