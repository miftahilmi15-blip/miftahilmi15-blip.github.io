

// =========================
// ELEMENTS
// =========================
const surahList = document.getElementById('surahList');
const modal = document.getElementById('modal');
const content = document.getElementById('content');
const title = document.getElementById('title');
const audio = new Audio();
let audioList = [];
let audioIndex = 0;

// =========================
// MODE MALAM
// =========================
function toggleDark() {
    document.body.classList.toggle('dark');
}

// =========================
// LOAD SURAH LIST
// =========================
async function loadSurahList() {
    try {
        const res = await fetch('https://api.alquran.cloud/v1/surah');
        const js = await res.json();
        js.data.forEach(s => {
            const li = document.createElement('li');
            li.textContent = `${s.number}. ${s.name} (${s.englishName})`;
            li.onclick = () => openSurah(s.number, s.name);
            surahList.appendChild(li);
        });
    } catch (err) {
        alert('Gagal memuat daftar surah: ' + err.message);
    }
}

// =========================
// OPEN SURAH
// =========================
async function openSurah(no, name) {
    modal.style.display = 'block';
    title.innerText = `Surah ${name}`;
    content.innerHTML = '';
    audioList = [];
    audioIndex = 0;

    try {
        // Ambil mushaf Utsmani
        const arRes = await fetch(`https://api.alquran.cloud/v1/surah/${no}/quran-uthmani`);
        const arJson = await arRes.json();

        // Ambil terjemahan Indonesia
        const idRes = await fetch(`https://api.alquran.cloud/v1/surah/${no}/id.indonesian`);
        const idJson = await idRes.json();

        const mushaf = document.createElement('div');
        mushaf.className = 'mushaf';

        arJson.data.ayahs.forEach((a, i) => {
            // Audio per ayat
            audioList.push(`https://cdn.islamic.network/quran/audio/128/ar.alafasy/${a.number}.mp3`);
            audio.src = audioList[0];

            // Ayat Mushaf
            const span = document.createElement('span');
            span.innerHTML = `
                ${a.text}
                <span class="ayah-number" onclick="toggleTr(${i})">﴿${a.numberInSurah}﴾</span>
            `;
            mushaf.appendChild(span);

            // Terjemahan per ayat
            const tr = document.createElement('div');
            tr.className = 'translation';
            tr.id = 'tr-' + i;
            tr.innerText = idJson.data.ayahs[i].text;
            mushaf.appendChild(tr);
        });

        content.appendChild(mushaf);

    } catch (err) {
        alert('Gagal memuat surah: ' + err.message);
    }
}

// =========================
// TOGGLE TERJEMAHAN
// =========================
function toggleTr(i) {
    const el = document.getElementById('tr-' + i);
    el.style.display = el.style.display === 'block' ? 'none' : 'block';
}

// =========================
// AUDIO CONTROLS
// =========================
function playAudio() {
    if (!audio.src) return;
    audio.play();
}
function pauseAudio() {
    if (!audio.src) return;
    audio.pause();
}
function nextAudio() {
    if (audioIndex + 1 >= audioList.length) return;
    audioIndex++;
    audio.src = audioList[audioIndex];
    audio.play();
}
function prevAudio() {
    if (audioIndex - 1 < 0) return;
    audioIndex--;
    audio.src = audioList[audioIndex];
    audio.play();
}

// =========================
// CLOSE MODAL
// =========================
document.querySelector('.close').onclick = () => {
    modal.style.display = 'none';
    audio.pause();
};

// =========================
// CLICK OUTSIDE MODAL
// =========================
window.onclick = e => {
    if (e.target === modal) {
        modal.style.display = 'none';
        audio.pause();
    }
};

// =========================
// INIT
// =========================
loadSurahList();
