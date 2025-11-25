// app.js - simple logic using Firebase compat SDK
const authSection = document.getElementById('auth-section');
const appSection = document.getElementById('app-section');
const emailInput = document.getElementById('email');
const passInput = document.getElementById('password');
const btnLogin = document.getElementById('btn-login');
const btnRegister = document.getElementById('btn-register');
const btnLogout = document.getElementById('btn-logout');

const namaInput = document.getElementById('nama');
const kelasInput = document.getElementById('kelas');
const kamarInput = document.getElementById('kamar');
const statusSelect = document.getElementById('status');
const btnAbsen = document.getElementById('btn-absen');
const btnClear = document.getElementById('btn-clear');
const recordsDiv = document.getElementById('records');
const userEmailSpan = document.getElementById('user-email');

btnRegister.onclick = async () => {
  const email = emailInput.value.trim();
  const pass = passInput.value.trim();
  if (!email || !pass) return alert('Isi email & password untuk register');
  try {
    await auth.createUserWithEmailAndPassword(email, pass);
    alert('Registrasi berhasil. Silakan login.');
  } catch(e){ alert('Gagal register: '+e.message); }
};

btnLogin.onclick = async () => {
  const email = emailInput.value.trim();
  const pass = passInput.value.trim();
  if (!email || !pass) return alert('Isi email & password untuk login');
  try {
    await auth.signInWithEmailAndPassword(email, pass);
  } catch(e){ alert('Login gagal: '+e.message); }
};

btnLogout.onclick = async () => {
  await auth.signOut();
};

btnClear.onclick = () => {
  namaInput.value=''; kelasInput.value=''; kamarInput.value=''; statusSelect.value='Hadir';
};

btnAbsen.onclick = async () => {
  const nama = namaInput.value.trim();
  const kelas = kelasInput.value.trim();
  const kamar = kamarInput.value.trim();
  const status = statusSelect.value;
  if (!nama || !kelas || !kamar) return alert('Lengkapi Nama, Kelas, Kamar.');
  try {
    await db.collection('attendance').add({
      nama, kelas, kamar, status,
      createdAt: firebase.firestore.FieldValue.serverTimestamp(),
      user: auth.currentUser ? auth.currentUser.email : null
    });
    alert('Absensi tersimpan.');
    btnClear.click();
  } catch(e){ alert('Gagal simpan: '+e.message); }
};

// Auth state
auth.onAuthStateChanged(user => {
  if (user) {
    authSection.classList.add('hidden');
    appSection.classList.remove('hidden');
    userEmailSpan.textContent = user.email;
  } else {
    authSection.classList.remove('hidden');
    appSection.classList.add('hidden');
    userEmailSpan.textContent = '';
  }
});

// Listen to attendance collection
db.collection('attendance').orderBy('createdAt', 'desc').limit(100)
.onSnapshot(snap => {
  recordsDiv.innerHTML = '';
  snap.forEach(doc => {
    const d = doc.data();
    const time = d.createdAt && d.createdAt.toDate ? d.createdAt.toDate().toLocaleString() : '-';
    const div = document.createElement('div');
    div.className = 'record';
    div.innerHTML = '<div><strong>'+ (d.nama||'') +'</strong> - '+ (d.status||'') +'</div>'
                  +'<div class="meta">Kelas: '+(d.kelas||'')+' • Kamar: '+(d.kamar||'')+' • '+time+'</div>';
    recordsDiv.appendChild(div);
  });
});
