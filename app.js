// ==========================================
// 1. KONFIGURASI FIREBASE
// ==========================================
firebase.initializeApp({
  apiKey: "AIzaSyAQ1A9rtEoEYoriA5Y7oSB84Fd1Xnu6aes",
  authDomain: "e-santri-ed555.firebaseapp.com",
  projectId: "e-santri-ed555"
});

const auth = firebase.auth();
auth.setPersistence(firebase.auth.Auth.Persistence.LOCAL);

// ==========================================
// 2. ELEMENT SELECTORS
// ==========================================
const elements = {
  authCard:      document.getElementById('login-card'),
  dashboard:     document.getElementById('dashboard'),
  loadingScreen: document.getElementById('loading-screen'),
  email:         document.getElementById('email'),
  pass:          document.getElementById('password'),
  msg:           document.getElementById('msg'),
  menuBtn:       document.getElementById('menu-btn'),
  sidebar:       document.getElementById('sidebar'),
  overlay:       document.getElementById('overlay'),
  userName:      document.getElementById('sidebar-name'),
  userEmail:     document.getElementById('sidebar-email'),
  userPhoto:     document.getElementById('user-photo'),
  welcomeMsg:    document.getElementById('welcome-msg')
};

// ==========================================
// 3. FUNGSI OTENTIKASI
// ==========================================
async function login() {
  const email = elements.email.value.trim();
  const pass  = elements.pass.value.trim();

  if (!email || !pass) return showMsg("Masukkan email dan password.", "error");

  try {
    // Cek metode sign-in (Mencegah salah metode jika user terdaftar via Google)
    const methods = await auth.fetchSignInMethodsForEmail(email);
    if (methods.includes("google.com") && !methods.includes("password")) {
      return showMsg("Gunakan tombol 'Google Login' untuk akun ini.", "error");
    }

    await auth.signInWithEmailAndPassword(email, pass);
    showMsg("Berhasil masuk!", "success");
  } catch (e) {
    let errorMap = {
      'auth/invalid-credential': "Email atau Password salah.",
      'auth/user-not-found': "Akun tidak terdaftar.",
      'auth/wrong-password': "Password salah."
    };
    showMsg(errorMap[e.code] || "Gagal masuk: " + e.message, "error");
  }
}

async function loginWithGoogle() {
  const provider = new firebase.auth.GoogleAuthProvider();
  try {
    await auth.signInWithPopup(provider);
  } catch (e) {
    showMsg("Gagal login Google.", "error");
  }
}

function register() {
  const email = elements.email.value.trim();
  const pass  = elements.pass.value.trim();

  if (pass.length < 6) return showMsg("Password minimal 6 karakter.", "error");

  auth.createUserWithEmailAndPassword(email, pass)
    .then(() => showMsg("Akun berhasil dibuat!", "success"))
    .catch(e => {
        if(e.code === 'auth/email-already-use') showMsg("Email sudah terdaftar.", "error");
        else showMsg(e.message, "error");
    });
}

function logout() {
  auth.signOut().then(() => {
    // Hapus remember me jika diinginkan
    localStorage.removeItem("e_santri_email");
    localStorage.removeItem("e_santri_pass");
    window.location.reload();
  });
}

// ==========================================
// 4. UI HANDLERS & STATE LISTENER
// ==========================================
function showMsg(text, type) {
  if (!elements.msg) return;
  elements.msg.textContent = text;
  elements.msg.style.color = type === "success" ? "#1f6f51" : "#d63031";
  setTimeout(() => elements.msg.textContent = "", 4000);
}

auth.onAuthStateChanged(user => {
  if (user) {
    elements.authCard.classList.add('hidden');
    elements.dashboard.classList.remove('hidden');
    elements.menuBtn.style.display = 'flex';
    
    // Update data UI
    elements.userName.textContent   = user.displayName || "Santri";
    elements.userEmail.textContent  = user.email;
    elements.userPhoto.src          = user.photoURL || "assets/default-avatar.png";
    if(elements.welcomeMsg) elements.welcomeMsg.innerText = `Ahlan, ${user.displayName || 'Santri'}!`;
  } else {
    elements.authCard.classList.remove('hidden');
    elements.dashboard.classList.add('hidden');
    elements.menuBtn.style.display = 'none';
  }

  // Sembunyikan Loading Screen (Sinkron dengan CSS transisi 0.5s)
  if (elements.loadingScreen) {
    elements.loadingScreen.style.opacity = '0';
    setTimeout(() => elements.loadingScreen.style.display = 'none', 500);
  }
});

// Sidebar Control
if (elements.menuBtn) {
  elements.menuBtn.onclick = () => {
    elements.sidebar.classList.add('open');
    elements.overlay.classList.add('show');
  };
}

elements.overlay.onclick = () => {
  elements.sidebar.classList.remove('open');
  elements.overlay.classList.remove('show');
};

function goTo(page) {
  document.body.style.opacity = '0.5';
  window.location.href = page;
}
