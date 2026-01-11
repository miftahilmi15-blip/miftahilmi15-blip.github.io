let currentPage = 1;
const totalPages = 604;

const surahContent = document.getElementById("surahContent");
const pageNumber = document.getElementById("pageNumber");

// tampilkan halaman
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

function nextPage() {
  if (currentPage < totalPages) {
    currentPage++;
    renderPage();
  }
}

function prevPage() {
  if (currentPage > 1) {
    currentPage--;
    renderPage();
  }
}

function toggleDark() {
  document.body.classList.toggle("dark");
}

// render pertama kali
renderPage();
