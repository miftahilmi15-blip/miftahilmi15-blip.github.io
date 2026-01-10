const surahContent = document.getElementById("surahContent");
const pageNumberEl = document.getElementById("pageNumber");

const svgUrls = [
  "https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip/main/sgv/001.svg",
  "https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip/main/sgv/002.svg",
  "https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip/main/sgv/003.svg",
  // ... lanjut sampai 604
];

let currentPage = 0;

function showPage(page){
  fetch(svgUrls[page])
    .then(res => {
      if(!res.ok) throw new Error("404 SVG");
      return res.text();
    })
    .then(svg => {
      surahContent.innerHTML = svg;
      pageNumberEl.textContent = `${page + 1} / ${svgUrls.length}`;
    })
    .catch(e => {
      surahContent.innerHTML = "<p>Gagal load halaman SVG</p>";
      console.error(e);
    });
}

function nextPage(){
  if(currentPage < svgUrls.length - 1){
    currentPage++;
    showPage(currentPage);
  }
}

function prevPage(){
  if(currentPage > 0){
    currentPage--;
    showPage(currentPage);
  }
}

function toggleDark(){
  document.body.classList.toggle("dark");
}

// Tampilkan halaman pertama saat load
showPage(currentPage);
