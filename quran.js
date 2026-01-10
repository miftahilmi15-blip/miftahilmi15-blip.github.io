const surahContent = document.getElementById("surahContent");
const pageNumberEl = document.getElementById("pageNumber");

// 🔹 List URL SVG (buat Python sudah generate 604 URL)
const svgUrls = [
  "https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip/main/sgv/001.svg",
  "https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip/main/sgv/002.svg",
  "https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip/main/sgv/003.svg",
  // ... sampai 604
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
        pageNumberEl.textContent = page + 1;
    })
    .catch(e => surahContent.innerHTML = "<p>Gagal load halaman SVG</p>");
}

function nextPage(){
  if(currentPage < svgUrls.length - 1) currentPage++;
  showPage(currentPage);
}

function prevPage(){
  if(currentPage > 0) currentPage--;
  showPage(currentPage);
}

// Mode malam
function toggleDark(){
  document.body.classList.toggle("dark");
}

// Tampilkan halaman pertama saat load
showPage(currentPage);
