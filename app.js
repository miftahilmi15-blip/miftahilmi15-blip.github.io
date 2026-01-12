// ==========================================
// 1. KONFIGURASI & INISIALISASI FIREBASE
// ==========================================
firebase.initializeApp({
  apiKey: "AIzaSyAQ1A9rtEoEYoriA5Y7oSB84Fd1Xnu6aes",
  authDomain: "e-santri-ed555.firebaseapp.com",
  projectId: "e-santri-ed555"
});

const auth = firebase.auth();
auth.setPersistence(firebase.auth.Auth.Persistence.LOCAL);

// ==========================================
// 2. ELEMENT SELECTORS (Disesuaikan dengan UI Mewah)
// ==========================================
const elements = {
  authCard:    document.getElementById('login-card'),
  dashboard:   document.getElementById('dashboard'),
  email:       document.getElementById('email'),
  pass:        document.getElementById('password'),
  msg:         document.getElementById('msg'),
  menuBtn:     document.getElementById('menu-btn'),
  sidebar:     document.getElementById('sidebar'),
  overlay:     document.getElementById('overlay'),
  userName:    document.getElementById('sidebar-name'),
  userEmail:   document.getElementById('sidebar-email'),
  userPhoto:   document.getElementById('user-photo')
};

// ==========================================
// 3. FUNGSI OTENTIKASI (Login, Register, Google)
// ==========================================
async function login() {
  const email = elements.email.value.trim();
  const pass  = elements.pass.value.trim();

  if (!email || !pass) return showMsg("Silakan lengkapi email dan password.", "warning");

  try {
    const methods = await auth.fetchSignInMethodsForEmail(email);
    
    if (methods.includes("google.com") && !methods.includes("password")) {
      return showMsg("Gunakan tombol 'Login Google' untuk akun ini.", "info");
    }

    await auth.signInWithEmailAndPassword(email, pass);
    showMsg("Berhasil masuk!", "success");
  } catch (e) {
    showMsg("Login Gagal: " + e.message, "error");
  }
}

async function loginWithGoogle() {
  const provider = new firebase.auth.GoogleAuthProvider();
  try {
    await auth.signInWithPopup(provider);
    showMsg("Berhasil masuk dengan Google!", "success");
  } catch (e) {
    showMsg("Gagal login Google: " + e.message, "error");
  }
}

function register() {
  const email = elements.email.value.trim();
  const pass  = elements.pass.value.trim();

  if (pass.length < 6) return showMsg("Password minimal 6 karakter.", "warning");

  auth.createUserWithEmailAndPassword(email, pass)
    .then(() => showMsg("Akun dibuat! Silakan masuk.", "success"))
    .catch(e => showMsg(e.message, "error"));
}

function logout() {
  auth.signOut().then(() => window.location.reload());
}

// ==========================================
// 4. UI HANDLERS (Sidebar & Popups)
// ==========================================
function showMsg(text, type) {
  if (!elements.msg) return;
  elements.msg.textContent = text;
  elements.msg.style.color = type === "success" ? "#0f4c3a" : "#e74c3c";
  // Hilangkan pesan setelah 4 detik
  setTimeout(() => elements.msg.textContent = "", 4000);
}

// State Listener: Otomatis ganti tampilan saat login/logout
auth.onAuthStateChanged(user => {
  if (user) {
    elements.authCard.classList.add('hidden');
    elements.dashboard.classList.remove('hidden');
    elements.menuBtn.style.display = 'flex';
    
    // Update data sidebar
    elements.userName.textContent  = user.displayName || "Santri";
    elements.userEmail.textContent = user.email;
    elements.userPhoto.src         = user.photoURL || "assets/default-avatar.png";
  } else {
    elements.authCard.classList.remove('hidden');
    elements.dashboard.classList.add('hidden');
    elements.menuBtn.style.display = 'none';
  }
});

// Sidebar Controls
elements.menuBtn.onclick = () => {
  elements.sidebar.classList.add('open');
  elements.overlay.classList.add('show');
};

const closeSidebar = () => {
  elements.sidebar.classList.remove('open');
  elements.overlay.classList.remove('show');
};

elements.overlay.onclick = closeSidebar;

// ==========================================
// 5. FITUR PENDUKUNG (WA Report & Navigation)
// ==========================================
function sendReport() {
  const user = auth.currentUser;
  const pesan = prompt("Tuliskan pengaduan/pesan Anda:");
  
  if (!pesan) return;

  const adminNumber = "6289661946783";
  const text = `*PENGADUAN E-SANTRI*\n\nNama: ${user.displayName || 'Santri'}\nEmail: ${user.email}\n\nPesan:\n${pesan}`;
  
  window.open(`https://wa.me/${adminNumber}?text=${encodeURIComponent(text)}`, "_blank");
}

function goTo(page) {
  // Animasi transisi keluar (opsional)
  document.body.style.opacity = '0';
  setTimeout(() => window.location.href = page, 300);
}

// Global Error Catching
window.addEventListener("unhandledrejection", e => console.error("Error:", e.reason));
