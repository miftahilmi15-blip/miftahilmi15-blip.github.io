let surahList = document.getElementById('surahList');
let modal = document.getElementById('modal');
let surahTitle = document.getElementById('surahTitle');
let surahContent = document.getElementById('surahContent');
let audio = new Audio();
let currentAudioIndex = 0;
let audioList = [];

function toggleDark(){
  document.body.classList.toggle('dark');
}
function closeModal(){
  modal.style.display = 'none';
}
function playAudio(){
  if(audioList.length>0){
    audio.src = audioList[currentAudioIndex];
    audio.play();
  }
}
function pauseAudio(){ audio.pause(); }

async function loadSurahList(){
  const res = await fetch('assets/alquran/quran.json');
  const data = await res.json();
  data.surahs.forEach(s => {
    const li = document.createElement('li');
    li.textContent = `${s.number}. ${s.name} (${s.englishName})`;
    li.onclick = ()=>openSurah(s.number);
    surahList.appendChild(li);
  });
}
async function openSurah(no){
  const res = await fetch('assets/alquran/quran.json');
  const data = await res.json();
  const surah = data.surahs[no-1];

  modal.style.display='block';
  surahTitle.innerText = `${surah.name} (${surah.englishName})`;
  surahContent.innerHTML='';

  audioList = [];
  currentAudioIndex = 0;

  surah.ayahs.forEach((a,i)=>{
    const span = document.createElement('span');
    span.className='mushaf';
    span.innerHTML = `${a.text} <span class="ayah-number" onclick="toggleTranslation(${i})">﴿${a.numberInSurah}﴾</span>`;
    surahContent.appendChild(span);

    const tr = document.createElement('div');
    tr.className='translation';
    tr.id='tr-'+i;
    tr.innerText = a.translation;
    surahContent.appendChild(tr);

    audioList.push(`assets/alquran/audio/${a.audio}`);
  });
}

function toggleTranslation(i){
  const el = document.getElementById('tr-'+i);
  el.style.display = el.style.display==='block'?'none':'block';
}

loadSurahList();
