let currentPage = 1;
const totalPages = 604;

const img = document.getElementById("mushafPage");
const pageNumber = document.getElementById("pageNumber");

function updatePage(){
  img.src = `svg/${String(currentPage).padStart(3,"0")}.svg`;
  pageNumber.textContent = currentPage;
}

function nextPage(){
  if(currentPage < totalPages){
    currentPage++;
    updatePage();
    saveLastPage();
  }
}

function prevPage(){
  if(currentPage > 1){
    currentPage--;
    updatePage();
    saveLastPage();
  }
}

function toggleDark(){
  document.body.classList.toggle("dark");
}

/* SIMPAN HALAMAN TERAKHIR */
function saveLastPage(){
  localStorage.setItem("lastPage", currentPage);
}

/* LOAD TERAKHIR DIBACA */
const last = localStorage.getItem("lastPage");
if(last){
  currentPage = parseInt(last);
  updatePage();
}
