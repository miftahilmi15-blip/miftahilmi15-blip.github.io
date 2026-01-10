// quran.js
const surahList = document.getElementById('surahList');
const modal = document.getElementById('modal');
const surahTitle = document.getElementById('surahTitle');
const surahContent = document.getElementById('surahContent');
let audio = new Audio();
let darkMode = false;

// Contoh data surah (bisa diambil dari API atau JSON)
const surahs = [
  { number: 1, name: "Al-Fatihah", ayahs: ["Bismillahirrahmanirrahim","Alhamdulillahi rabbil 'alamin","Ar-Rahmanir-Rahim","Maliki yaumiddin","Iyyaka na'budu wa iyyaka nasta'in","Ihdinas siratal mustaqim","Siratal-ladhina an'amta 'alaihim ghayril maghdubi 'alaihim walad-dallin"] },
  { number: 2, name: "Al-Baqarah", ayahs: ["Alif Lam Mim","Dzalika alkitabu la rayba fihi hudal lilmuttaqin","Alladhina yu'minuna bil-ghaybi","Wa yuqimuna as-salata","Wa mimma razaqnahum yunfiqun"] },
  // Tambahkan surah lainnya
];

// Render daftar surah
surahs.forEach(surah=>{
  const li = document.createElement('li');
  li.innerText = `${surah.number}. ${surah.name}`;
  li.style.cursor = 'pointer';
  li.onclick = ()=>openModal(surah);
  surahList.appendChild(li);
});

function openModal(surah){
  surahTitle.innerText = `${surah.number}. ${surah.name}`;
  surahContent.innerHTML = '';
  surah.ayahs.forEach((ayah,i)=>{
    const p = document.createElement('p');
    p.innerText = `${i+1}. ${ayah}`;
    surahContent.appendChild(p);
  });

  // Ganti audio (contoh URL dummy, ganti dengan file MP3 asli)
  audio.src = `audio/surah${surah.number}.mp3`;
  modal.style.display = 'flex';
}

function closeModal(){
  modal.style.display = 'none';
  audio.pause();
}

function playAudio(){ audio.play(); }
function pauseAudio(){ audio.pause(); }

function toggleDark(){
  document.body.classList.toggle("dark");
}

