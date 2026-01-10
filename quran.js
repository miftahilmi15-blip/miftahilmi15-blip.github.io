const surahContent = document.getElementById("surahContent");
const pageNumberEl = document.getElementById("pageNumber");

// Generate 001.svg sampai 604.svg
const svgUrls = Array.from({length: 604}, (_, i) =>
  `https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip/main/svg/${String(i+1).padStart(3,'0')}.svg`
);

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
