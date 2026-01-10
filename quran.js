const surahList    = document.getElementById("surahList");
const modal        = document.getElementById("modal");
const surahTitle   = document.getElementById("surahTitle");
const surahContent = document.getElementById("surahContent");

let audio = new Audio();

/* ===============================
   LOAD LIST 114 SURAH
================================ */
fetch("https://api.alquran.cloud/v1/surah")
  .then(res => res.json())
  .then(res => {
    surahList.innerHTML = "";
    res.data.forEach(surah => {
      const li = document.createElement("li");
      li.textContent = `${surah.number}. ${surah.name} (${surah.englishName})`;
      li.onclick = () => loadSurah(surah.number);
      surahList.appendChild(li);
    });
  });

/* ===============================
   LOAD SURAH (UTHMANI)
================================ */
function loadSurah(number) {
  surahTitle.textContent = "Memuat surah...";
  surahContent.innerHTML = "";

  fetch(`https://api.alquran.cloud/v1/surah/${number}/quran-uthmani`)
    .then(res => res.json())
    .then(res => {
      const surah = res.data;
      surahTitle.textContent =
        `${surah.number}. ${surah.name} — ${surah.englishName}`;

      surah.ayahs.forEach(ayah => {
        const ayahEl = document.createElement("div");
        ayahEl.className = "ayah";

        ayahEl.innerHTML = `
          ${ayah.text}
          <span class="ayah-number">﴿${ayah.numberInSurah}﴾</span>
        `;

        surahContent.appendChild(ayahEl);
      });

      audio.src = `https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/${number}.mp3`;
      modal.style.display = "block";
    });
}

/* ===============================
   MODAL CONTROL
================================ */
function closeModal() {
  modal.style.display = "none";
  audio.pause();
  audio.currentTime = 0;
}

function playAudio() {
  audio.play();
}

function pauseAudio() {
  audio.pause();
}

/* ===============================
   DARK MODE
================================ */
function toggleDark() {
  document.body.classList.toggle("dark");
}
