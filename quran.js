const surahContent = document.getElementById("surahContent");
const pageNumberEl = document.getElementById("pageNumber");

let currentPage = 1;
const TOTAL = 604;

function showPage(page){
  surahContent.innerHTML = `
    <object 
      type="image/svg+xml" 
      data="svg/${String(page).padStart(3,'0')}.svg" 
      width="100%">
    </object>
  `;
  pageNumberEl.textContent = page;
}

function nextPage(){
  if(currentPage < TOTAL){
    currentPage++;
    showPage(currentPage);
  }
}

function prevPage(){
  if(currentPage > 1){
    currentPage--;
    showPage(currentPage);
  }
}

function toggleDark(){
  document.body.classList.toggle("dark");
}

document.addEventListener("DOMContentLoaded", () => {
  showPage(currentPage);
});
