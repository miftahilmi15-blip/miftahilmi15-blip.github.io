const surahContent = document.getElementById("surahContent");
const pageNumberEl = document.getElementById("pageNumber");

const svgUrls = [
  "https://raw.githubusercontent.com/miftahilmi15-blip/miftahilmi15-blip.github.io/main/svg/034.svg"
];

let currentPage = 0;

function showPage(page) {
  fetch(svgUrls[page])
    .then(res => {
      if (!res.ok) throw new Error("404 SVG");
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

// Tes tombol navigasi (meskipun hanya 1 halaman)
function nextPage() {}
function prevPage() {}
function toggleDark() {
  document.body.classList.toggle("dark");
}

document.addEventListener("DOMContentLoaded", () => {
  showPage(currentPage);
});
