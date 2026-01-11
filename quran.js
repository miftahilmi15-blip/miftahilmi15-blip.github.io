document.addEventListener("DOMContentLoaded", function () {

  const surahSelect = document.getElementById("surahSelect");
  const content = document.getElementById("content");

  // ambil daftar surah
  fetch("https://api.quran.gading.dev/surah")
    .then(res => res.json())
    .then(data => {
      surahSelect.innerHTML = "";

      data.data.forEach(surah => {
        const opt = document.createElement("option");
        opt.value = surah.number;
        opt.textContent =
          surah.number + ". " + surah.name.transliteration.id;
        surahSelect.appendChild(opt);
      });

      loadSurah(1);
    })
    .catch(() => {
      content.innerHTML = "Gagal memuat daftar surah";
    });

  surahSelect.addEventListener("change", function () {
    loadSurah(this.value);
  });

  function loadSurah(no) {
    content.innerHTML = "Memuat ayat...";

    fetch(`https://api.quran.gading.dev/surah/${no}`)
      .then(res => res.json())
      .then(data => {
        content.innerHTML = "";

        data.data.verses.forEach(v => {
          const div = document.createElement("div");
          div.className = "ayah";
          div.innerHTML = `
            <div class="arab">${v.text.arab}</div>
            <div class="arti">${v.translation.id}</div>
          `;
          content.appendChild(div);
        });
      })
      .catch(() => {
        content.innerHTML = "Gagal memuat ayat";
      });
  }

});

