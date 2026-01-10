
// =========================
// ELEMENTS
// =========================
const authSection   = document.getElementById('login-card'); // card login/register
const appSection    = document.getElementById('dashboard');  // dashboard setelah login
const emailInput    = document.getElementById('email');
const passInput     = document.getElementById('password');
const btnLogin      = document.querySelector('.btn.primary');
const btnRegister   = document.querySelector('.btn.secondary');

const menuBtn       = document.getElementById('menu-btn');
const closeBtn      = document.getElementById('close-btn');
const overlay       = document.getElementById('overlay');
const sidebar       = document.getElementById('sidebar');

const userNameEl    = document.getElementById('sidebar-name');
const userEmailSpan = document.getElementById('sidebar-email');
const userPhotoEl   = document.getElementById('user-photo');


// =========================
// FIREBASE INITIALIZE
// =========================
firebase.initializeApp({
  apiKey: "AIzaSyAQ1A9rtEoEYoriA5Y7oSB84Fd1Xnu6aes",
  authDomain: "e-santri-ed555.firebaseapp.com",
  projectId: "e-santri-ed555"
});

const auth = firebase.auth();

// =========================
// AUTH PERSISTENCE
// =========================
auth.setPersistence(firebase.auth.Auth.Persistence.LOCAL)
  .catch(e => console.error("Persistence error:", e));


// =========================
// AUTH FUNCTIONS
// =========================
async function login() {
  const email = emailInput.value.trim();
  const pass  = passInput.value.trim();

  if (!email || !pass) {
    return showMsg("Isi email & password");
  }

  try {
    // 🔍 CEK PROVIDER AKUN
    const methods = await auth.fetchSignInMethodsForEmail(email);

    // 🚫 AKUN GOOGLE-ONLY
    if (methods.includes("google.com") && !methods.includes("password")) {
      showMsg(
        "Akun ini terdaftar menggunakan Google.\n" +
        "Silakan login dengan Google atau reset password."
      );
      return;
    }

    // ✅ LOGIN EMAIL & PASSWORD
    await auth.signInWithEmailAndPassword(email, pass);

  } catch (e) {
    showMsg("Login gagal: " + e.message);
  }
}

function register() {
  const email = emailInput.value.trim();
  const pass  = passInput.value.trim();

  if (!email || !pass) {
    return showMsg("Isi email & password untuk register");
  }

  auth.createUserWithEmailAndPassword(email, pass)
    .then(() => showMsg("Akun berhasil dibuat, silakan login"))
    .catch(e => showMsg("Gagal register: " + e.message));
}

function logout() {
  auth.signOut().then(() => {
    window.location.href = "index.html";
  });
}


// =========================
// MESSAGE HANDLER
// =========================
function showMsg(message) {
  const el = document.getElementById('msg');
  if (!el) return;
  el.textContent = message;
}


// =========================
// AUTH STATE LISTENER
// =========================
auth.onAuthStateChanged(user => {
  if (user) {
    authSection.classList.add('hidden');
    appSection.classList.remove('hidden');
    menuBtn.style.display = 'block';

    userNameEl.textContent    = user.displayName || "Pengguna";
    userEmailSpan.textContent = user.email;
    userPhotoEl.src           = user.photoURL || "assets/default-avatar.png";
  } else {
    authSection.classList.remove('hidden');
    appSection.classList.add('hidden');
    menuBtn.style.display = 'none';

    userNameEl.textContent    = "Pengguna";
    userEmailSpan.textContent = "";
    userPhotoEl.src           = "assets/default-avatar.png";
  }
});


// =========================
// SIDEBAR MENU
// =========================
menuBtn.onclick = () => {
  sidebar.classList.add('open');
  overlay.classList.add('show');
};

closeBtn.onclick = closeSidebar;
overlay.onclick  = closeSidebar;

function closeSidebar() {
  sidebar.classList.remove('open');
  overlay.classList.remove('show');
}


// =========================
// EDIT PROFILE
// =========================
function openEdit() {
  document.getElementById('edit-profile-popup').classList.add('show');
}

function closeEdit() {
  document.getElementById('edit-profile-popup').classList.remove('show');
}

async function saveProfile() {
  const user = auth.currentUser;
  if (!user) return alert("Tidak ada user login");

  const name        = document.getElementById('edit-name').value.trim();
  const newEmail    = document.getElementById('edit-email').value.trim();
  const newPassword = document.getElementById('edit-pass').value.trim();

  try {
    // 🔐 RE-AUTH WAJIB
    const currentPassword = prompt("Masukkan password lama untuk konfirmasi:");
    if (!currentPassword) return;

    const credential = firebase.auth.EmailAuthProvider.credential(
      user.email,
      currentPassword
    );

    await user.reauthenticateWithCredential(credential);

    // ✅ UPDATE DATA
    if (name)        await user.updateProfile({ displayName: name });
    if (newEmail)    await user.updateEmail(newEmail);
    if (newPassword) await user.updatePassword(newPassword);

    alert("Profil berhasil diperbarui!");
    closeEdit();

  } catch (e) {
    alert("Gagal update: " + e.message);
  }
}


// =========================
// WHATSAPP REPORT
// =========================
function openWAReport() {
  document.getElementById("wa-report-popup").style.display = "flex";
}

function closeWAReport() {
  document.getElementById("wa-report-popup").style.display = "none";
}

function sendReport() {
  const user  = auth.currentUser;
  const pesan = document.getElementById("wa-message").value.trim();
  if (!pesan) return alert("Isi pengaduannya dulu ya!");

  const name  = user.displayName || "Santri";
  const email = user.email;
  const adminNumber = "6289661946783";

  const text = `
Pengaduan Santri:
Nama: ${name}
Email: ${email}

Pesan:
${pesan}
  `;

  window.open(
    `https://wa.me/${adminNumber}?text=${encodeURIComponent(text)}`,
    "_blank"
  );

  closeWAReport();
}


// =========================
// NAVIGATION
// =========================
function goTo(page) {
  window.location.href = page;
}


// =========================
// GLOBAL ERROR SAFETY
// =========================
window.addEventListener("unhandledrejection", e => {
  console.error("Unhandled error:", e.reason);
});
