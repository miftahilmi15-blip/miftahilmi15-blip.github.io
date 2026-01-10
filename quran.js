// ==============================
// Mushaf E-Santri JS
// ==============================
const surahContent = document.getElementById("surahContent");
const pageNumberEl = document.getElementById("pageNumber");

// Buat array otomatis dari 001 sampai 604 pakai jsDelivr
const svgUrls = Array.from({length: 604}, (_, i) =>
  `https://cdn.jsdelivr.net/gh/miftahilmi15-blip/miftahilmi15-blip.github.io/svg/${String(i+1).padStart(3,'0')}.svg`
);

let currentPage = 0;

// Tampilkan halaman tertentu
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

// Navigasi berikutnya
function nextPage(){
  if(currentPage < svgUrls.length - 1){
    currentPage++;
    showPage(currentPage);
  }
}

// Navigasi sebelumnya
function prevPage(){
  if(currentPage > 0){
    currentPage--;
    showPage(currentPage);
  }
}

// Mode malam
function toggleDark(){
  document.body.classList.toggle("dark");
}

// Tunggu sampai DOM siap sebelum show page pertama
document.addEventListener("DOMContentLoaded", () => {
  showPage(currentPage);

  // Tambahkan shortcut keyboard (panah kiri/kanan)
  document.addEventListener("keydown", e => {
    if(e.key === "ArrowRight") nextPage();
    if(e.key === "ArrowLeft") prevPage();
  });
});
