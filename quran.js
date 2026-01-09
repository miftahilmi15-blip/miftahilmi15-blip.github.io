const surahList = document.getElementById('surah-list');
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const modalBody = document.getElementById('modal-body');

const audio = new Audio();
let audioList=[],audioIndex=0;

// Mode malam
function toggleDark(){ document.body.classList.toggle('dark'); }

// Load daftar surah
async function getSurahList(){
  const res = await fetch('https://api.alquran.cloud/v1/surah');
  const data = await res.json();
  data.data.forEach(s=>{
    const li = document.createElement('li');
    li.textContent = `${s.number}. ${s.name} (${s.englishName}) - ${s.numberOfAyahs} ayat`;
    li.onclick = ()=> openSurah(s.number,s.name);
    surahList.appendChild(li);
  });
}

// Buka surah
async function openSurah(no,name){
  modal.style.display='block';
  modalTitle.innerText = `Surah ${name}`;
  modalBody.innerHTML='';
  audioList=[]; audioIndex=0;

  const ar = await fetch(`https://api.alquran.cloud/v1/surah/${no}/quran-uthmani`).then(r=>r.json());
  const id = await fetch(`https://api.alquran.cloud/v1/surah/${no}/id.indonesian`).then(r=>r.json());

  const mushaf = document.createElement('div');
  mushaf.className='mushaf';

  // Pisahkan Bismillah jika ada
  let firstAyah = ar.data.ayahs[0].text;
  if(firstAyah.startsWith("بسم الله الرحمن الرحيم")){
    const basmalahDiv = document.createElement('div');
    basmalahDiv.className='basmalah';
    basmalahDiv.innerText='بسم الله الرحمن الرحيم';
    mushaf.appendChild(basmalahDiv);
    // hapus Bismillah dari ayat pertama
    ar.data.ayahs[0].text = firstAyah.replace("بسم الله الرحمن الرحيم","").trim();
  }

  ar.data.ayahs.forEach((a,i)=>{
    audioList.push(`https://cdn.islamic.network/quran/audio/128/ar.alafasy/${a.number}.mp3`);
    if(i==0) audio.src = audioList[0];

    const span = document.createElement('span');
    span.innerHTML = `
      ${a.text}
      <span class="ayah-number" onclick="toggleTr(${i})">﴿${a.numberInSurah}﴾</span>
    `;
    mushaf.appendChild(span);

    const tr = document.createElement('div');
    tr.className='translation';
    tr.id = 'tr-'+i;
    tr.innerText = id.data.ayahs[i].text;
    mushaf.appendChild(tr);
  });

  modalBody.appendChild(mushaf);
}

// Toggle terjemahan
function toggleTr(i){
  const el = document.getElementById('tr-'+i);
  el.style.display = el.style.display==='block'?'none':'block';
}

// Audio control
function playAudio(){ audio.play(); }
function pauseAudio(){ audio.pause(); }

getSurahList();
