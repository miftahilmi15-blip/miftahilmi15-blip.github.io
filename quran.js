const surahContent = document.getElementById("surahContent");
const pageNumberEl = document.getElementById("pageNumber");

// Array otomatis dari 001 sampai 604 via jsDelivr
const svgUrls = Array.from({length: 604}, (_, i) =>
  `https://cdn.jsdelivr.net/gh/miftahilmi15-blip/miftahilmi15-blip.github.io/svg/${String(i+1).padStart(3,'0')}.svg`
);

let currentPage = 0;

function showPage(page){
  if(page < 0 || page >= svgUrls.length) return;

  fetch(svgUrls[page])
    .then(res => {
      if(!res.ok) throw new Error(`Gagal load SVG halaman ${page+1}`);
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

function nextPage(){ if(currentPage < svgUrls.length-1){ currentPage++; showPage(currentPage); } }
function prevPage(){ if(currentPage>0){ currentPage--; showPage(currentPage); } }
function toggleDark(){ document.body.classList.toggle("dark"); }

document.addEventListener("DOMContentLoaded", () => { showPage(currentPage); });
