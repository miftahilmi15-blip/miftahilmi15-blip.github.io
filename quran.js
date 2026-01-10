const surahList = document.getElementById("surahList");
const modal = document.getElementById("modal");
const surahTitle = document.getElementById("surahTitle");
const surahContent = document.getElementById("surahContent");

let audio = new Audio();

// 🔹 LOAD SEMUA SURAH (114)
fetch("https://api.alquran.cloud/v1/surah")
  .then(res => res.json())
  .then(data => {
    data.data.forEach(surah => {
      const li = document.createElement("li");
      li.textContent = `${surah.number}. ${surah.englishName}`;
      li.onclick = () => loadSurah(surah.number, surah.name);
      surahList.appendChild(li);
    });
  });

function loadSurah(number, name) {
  surahTitle.textContent = `${number}. ${name}`;
  surahContent.innerHTML = "Memuat...";

  fetch(`https://api.alquran.cloud/v1/surah/${number}`)
    .then(res => res.json())
    .then(data => {
      surahContent.innerHTML = "";
      data.data.ayahs.forEach(ayah => {
        const p = document.createElement("p");
        p.innerHTML = `${ayah.text} <span class="ayah-number">﴿${ayah.numberInSurah}﴾</span>`;
        surahContent.appendChild(p);
      });

      audio.src = `https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/${number}.mp3`;
      modal.style.display = "flex";
    });
}

function closeModal() {
  modal.style.display = "none";
  audio.pause();
}

function playAudio() { audio.play(); }
function pauseAudio() { audio.pause(); }

function toggleDark() {
  document.body.classList.toggle("dark");
}
