alert("JS + API JALAN");

document.addEventListener("DOMContentLoaded", function () {

  const surahSelect = document.getElementById("surahSelect");
  const content = document.getElementById("content");

  // Ambil daftar surah
  fetch("https://api.quran.gading.dev/surah")
    .then(res => res.json())
    .then(json => {
      surahSelect.innerHTML = "";

      json.data.forEach(surah => {
        const option = document.createElement("option");
        option.value = surah.number;
        option.textContent =
          surah.number + ". " + surah.name.transliteration.id;
        surahSelect.appendChild(option);
      });

      loadSurah(1);
    })
    .catch(err => {
      content.innerHTML = "Gagal memuat daftar surah";
      console.error(err);
    });

  surahSelect.addEventListener("change", function () {
    loadSurah(this.value);
  });

  function loadSurah(no) {
    content.innerHTML = "Memuat ayat...";

    fetch(`https://api.quran.gading.dev/surah/${no}`)
      .then(res => res.json())
      .then(json => {
        content.innerHTML = "";

        json.data.verses.forEach(v => {
          const div = document.createElement("div");
          div.innerHTML = `
            <div style="font-size:24px; text-align:right;">
              ${v.text.arab}
            </div>
            <div style="color:gray; margin-bottom:15px;">
              ${v.translation.id}
            </div>
          `;
          content.appendChild(div);
        });
      })
      .catch(err => {
        content.innerHTML = "Gagal memuat ayat";
        console.error(err);
      });
  }

});

