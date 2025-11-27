// =========================
// ELEMENT LOGIN / REGISTER
// =========================
const authSection = document.getElementById('auth-section');
const appSection = document.getElementById('app-section');
const emailInput = document.getElementById('email');
const passInput = document.getElementById('password');
const btnLogin = document.getElementById('btn-login');
const btnRegister = document.getElementById('btn-register');
const btnLogout = document.getElementById('btn-logout');

const userEmailSpan = document.getElementById('user-email');


// =========================
// MENU TITIK TIGA (SIDEBAR)
// =========================
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");
const menuBtn = document.getElementById("menu-btn");
const closeBtn = document.getElementById("close-btn");

menuBtn.onclick = () => {
  sidebar.classList.add("open");
  overlay.classList.add("show");
};

closeBtn.onclick = () => {
  sidebar.classList.remove("open");
  overlay.classList.remove("show");
};

overlay.onclick = () => {
  sidebar.classList.remove("open");
  overlay.classList.remove("show");
};


// =========================
// LOGIN LISTENER
// =========================
auth.onAuthStateChanged(user => {
  if (user) {
    authSection.classList.add("hidden");
    appSection.classList.remove("hidden");

    userEmailSpan.textContent = user.email;
  } else {
    authSection.classList.remove("hidden");
    appSection.classList.add("hidden");

    userEmailSpan.textContent = "";
  }
});


// =========================
// REGISTER
// =========================
btnRegister.onclick = async () => {
  const email = emailInput.value.trim();
  const pass = passInput.value.trim();

  if (!email || !pass)
    return alert("Isi email & password untuk register");

  try {
    await auth.createUserWithEmailAndPassword(email, pass);
    alert("Registrasi berhasil. Silakan login.");
  } catch (e) {
    alert("Gagal register: " + e.message);
  }
};


// =========================
// LOGIN
// =========================
btnLogin.onclick = async () => {
  const email = emailInput.value.trim();
  const pass = passInput.value.trim();

  if (!email || !pass)
    return alert("Isi email & password untuk login");

  try {
    await auth.signInWithEmailAndPassword(email, pass);
  } catch (e) {
    alert("Login gagal: " + e.message);
  }
};


// =========================
// LOGOUT
// =========================
btnLogout.onclick = async () => {
  await auth.signOut();
};
