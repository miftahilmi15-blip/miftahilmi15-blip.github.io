from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- CONFIG AI ---
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

# Variabel ini menampung seluruh tampilan website Kakak
HTML_CODE = r'''
<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>E-Santri | Pro v16</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Noto+Naskh+Arabic:wght@700&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
<style>
  :root { --primary: #1f6f51; --primary-grad: linear-gradient(135deg, #1f6f51, #2ecc71); --bg: #f8faf9; --text: #2d3436; --shadow: 0 10px 30px rgba(31, 111, 81, 0.1); }
  * { margin: 0; padding: 0; box-sizing: border-box; font-family: "Poppins", sans-serif; -webkit-tap-highlight-color: transparent; }
  body { background: var(--bg); color: var(--text); min-height: 100vh; overflow-x: hidden; }
  .container { width: 100%; max-width: 420px; margin: 0 auto; padding: 20px; }
  .header-box { text-align: center; padding: 25px 0; }
  .title { font-family: 'Montserrat', sans-serif; font-size: 32px; font-weight: 900; color: var(--primary); letter-spacing: 1px; }
  .menu-trigger { position: fixed; top: 25px; right: 25px; z-index: 1400; background: white; color: var(--primary); width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 20px; box-shadow: var(--shadow); cursor: pointer; border: 1px solid #eee; }
  .sidebar { position: fixed; top: 0; right: -100%; width: 100%; height: 100%; background: rgba(255,255,255,0.98); z-index: 2000; transition: 0.5s; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px; }
  .sidebar.open { right: 0; }
  .close-sidebar { position: absolute; top: 30px; right: 30px; font-size: 30px; color: #ccc; cursor: pointer; }
  .user-profile { text-align: center; margin-bottom: 40px; }
  .user-profile img { width: 90px; height: 90px; border-radius: 25px; margin-bottom: 12px; box-shadow: var(--shadow); border: 3px solid white; }
  .sidebar-nav { display: flex; flex-direction: column; gap: 15px; width: 100%; max-width: 280px; }
  .sidebar-nav a { display: flex; align-items: center; justify-content: center; gap: 12px; padding: 16px; text-decoration: none; color: var(--text); font-weight: 600; background: white; border-radius: 18px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f0f0f0; }
  .streak-card { background: var(--primary-grad); border-radius: 24px; padding: 20px; color: white; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 15px 35px rgba(31,111,81,0.2); }
  .fire-icon { font-size: 40px; transition: 0.5s; filter: drop-shadow(0 0 10px rgba(255,165,0,0.8)); }
  .fire-off { filter: grayscale(1) opacity(0.3) !important; transform: scale(0.8); }
  .mahfuzat-box { background: white; padding: 15px 20px; border-radius: 50px; margin-bottom: 25px; display: flex; align-items: center; box-shadow: var(--shadow); border: 1px solid #f0f0f0; }
  .m-label { background: #d4b96a; color: white; font-size: 9px; font-weight: 800; padding: 5px 12px; border-radius: 50px; margin-right: 12px; }
  .menu-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
  .menu-item { background: white; padding: 22px 10px; border-radius: 24px; text-align: center; box-shadow: var(--shadow); transition: 0.3s; cursor: pointer; }
  .menu-item:active { transform: scale(0.9); }
  .menu-symbol { font-size: 32px; display: block; margin-bottom: 8px; }
  .menu-item span { font-size: 11px; font-weight: 700; color: #555; }
  .card-login { background: white; padding: 40px 30px; border-radius: 35px; box-shadow: var(--shadow); text-align: center; }
  .btn-google { width: 100%; padding: 14px; border-radius: 16px; border: 1.5px solid #eee; background: white; display: flex; align-items: center; justify-content: center; gap: 12px; font-weight: 700; color: #444; cursor: pointer; margin-top: 20px; }
  .btn-google img { width: 22px; height: 22px; }
  .hidden { display: none !important; }
  .msg-user { background: #1f6f51; color: white; padding: 8px; border-radius: 10px; margin-bottom: 8px; text-align: right; align-self: flex-end; max-width: 80%; }
  .msg-ai { background: #f1f1f1; color: #333; padding: 8px; border-radius: 10px; margin-bottom: 8px; text-align: left; align-self: flex-start; max-width: 80%; }
</style>

<script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-auth-compat.js"></script>
</head>
<body>

<div class="menu-trigger" id="menu-btn" style="display:none;"><i class="fa-solid fa-bars"></i></div>

<div class="sidebar" id="sidebar">
  <div class="close-sidebar" id="close-btn">✕</div>
  <div class="user-profile">
    <img id="u-img" src="https://ui-avatars.com/api/?background=1f6f51&color=fff&name=Santri">
    <h3 id="u-name">Santri</h3>
    <p id="u-email" style="color:#999; font-size:12px;"></p>
  </div>
  <div class="sidebar-nav">
    <a href="#" onclick="location.reload()"><i class="fa-solid fa-house"></i> Dashboard</a>
    <a href="#" onclick="logout()" style="color:#e74c3c;"><i class="fa-solid fa-power-off"></i> Keluar</a>
  </div>
</div>

<main class="container">
  <header class="header-box"><h1 class="title">E-SANTRI</h1></header>

  <div id="login-card" class="card-login hidden">
    <h2 style="color:var(--primary); margin-bottom:25px;">Ahlan wa Sahlan</h2>
    <input type="email" id="email" placeholder="Email Santri" style="width:100%; padding:15px; margin-bottom:12px; border-radius:12px; border:1px solid #eee;">
    <input type="password" id="password" placeholder="Password" style="width:100%; padding:15px; margin-bottom:20px; border-radius:12px; border:1px solid #eee;">
    <button onclick="login()" style="width:100%; padding:16px; border-radius:16px; border:none; background:var(--primary-grad); color:white; font-weight:700;">MASUK</button>
    <button class="btn-google" onclick="loginGoogle()">
      <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/pwa/google.svg"> Masuk dengan Google
    </button>
  </div>

  <section id="dashboard" class="hidden">
    <div class="streak-card">
      <div><p style="font-size:11px; opacity:0.8;">Hadir Hari Ini</p><h2 id="streak-text">0 Hari</h2></div>
      <div id="fire-api" class="fire-icon">🔥</div>
    </div>
    <div class="menu-grid">
      <div class="menu-item"><span>📖</span><br><span>Al-Quran</span></div>
      <div class="menu-item"><span>📝</span><br><span>Absensi</span></div>
      <div class="menu-item"><span>🏆</span><br><span>Tahfidz</span></div>
    </div>
  </section>
</main>

<div id="ai-button" onclick="toggleChat()" style="position: fixed; bottom: 20px; right: 20px; background: #15803d; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.2); z-index: 1000; display: none;">
    <span style="font-size: 24px;">🌙</span>
</div>

<div id="ai-window" style="display: none; position: fixed; bottom: 90px; right: 20px; width: 300px; height: 400px; background: white; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); z-index: 1000; flex-direction: column; overflow: hidden;">
    <div style="background: #15803d; color: white; padding: 10px; font-weight: bold; text-align: center;">Asisten E-Santri</div>
    <div id="chatContent" style="flex: 1; padding: 10px; overflow-y: auto; font-size: 14px; display: flex; flex-direction: column;">
        <div class="msg-ai">Assalamu'alaikum! Ada yang bisa saya bantu?</div>
    </div>
    <div style="padding: 10px; border-top: 1px solid #eee; display: flex;">
        <input type="text" id="aiInput" placeholder="Tanya sesuatu..." style="flex: 1; border: none; outline: none;" onkeypress="if(event.key==='Enter') kirimKeAI()">
        <button onclick="kirimKeAI()" style="color: #15803d; font-weight: bold; background: none; border: none; cursor: pointer;">Kirim</button>
    </div>
</div>

<script>
  const firebaseConfig = { apiKey: "AIzaSyCFVjE7ey5g__Iv4vUOZftB7g8GtSTSsEo", authDomain: "e-santri-b62be.firebaseapp.com", projectId: "e-santri-b62be", storageBucket: "e-santri-b62be.firebasestorage.app", messagingSenderId: "6560427635", appId: "1:6560427635:web:368b4fbf95163e8d214406" };
  firebase.initializeApp(firebaseConfig);
  const auth = firebase.auth();

  document.getElementById("menu-btn").onclick = () => { document.getElementById("sidebar").classList.add("open"); }
  document.getElementById("close-btn").onclick = () => { document.getElementById("sidebar").classList.remove("open"); }

  function toggleChat() { 
    const win = document.getElementById("ai-window");
    win.style.display = win.style.display === "none" ? "flex" : "none";
  }

  async function kirimKeAI() {
    const input = document.getElementById('aiInput');
    const box = document.getElementById('chatContent');
    const text = input.value.trim();
    if(!text) return;

    box.innerHTML += `<div class="msg-user">${text}</div>`;
    input.value = "";
    box.scrollTop = box.scrollHeight;

    const loadingId = "load-" + Date.now();
    box.innerHTML += `<div class="msg-ai" id="${loadingId}">...</div>`;

    try {
        const res = await fetch(window.location.origin + '/proses', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ pesan: text })
        });
        const d = await res.json();
        document.getElementById(loadingId).innerText = d.jawaban;
    } catch (e) {
        document.getElementById(loadingId).innerText = "Afwan, asisten sedang sinkronisasi.";
    }
    box.scrollTop = box.scrollHeight;
  }

  function login() { auth.signInWithEmailAndPassword(document.getElementById("email").value, document.getElementById("password").value).catch(e=>alert(e.message)); }
  function logout() { auth.signOut().then(()=>location.reload()); }
  function loginGoogle() { auth.signInWithRedirect(new firebase.auth.GoogleAuthProvider()); }

  auth.onAuthStateChanged(user => {
    if(user){
      document.getElementById("dashboard").classList.remove("hidden");
      document.getElementById("login-card").classList.add("hidden");
      document.getElementById("menu-btn").style.display="flex";
      document.getElementById("ai-button").style.display="flex";
      document.getElementById("u-name").innerText = user.displayName || "Santri";
      document.getElementById("u-email").innerText = user.email;
    } else {
      document.getElementById("login-card").classList.remove("hidden");
      document.getElementById("dashboard").classList.add("hidden");
    }
  });
</script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(silent=True, force=True)
        if not data or 'pesan' not in data:
            return jsonify({"jawaban": "Gagal menerima pesan."}), 400
        pesan_user = data.get('pesan')
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text if response.text else "AI tidak memberikan jawaban."})
    except Exception as e:
        return jsonify({"jawaban": f"Sistem Sibuk: {str(e)}"}), 500

app = app.getElementById(loadingId).innerText = "Afwan, asisten sedang sinkronisasi.";
    }
    box.scrollTop = box.scrollHeight;
  }

  function login() { auth.signInWithEmailAndPassword(document.getElementById("email").value, document.getElementById("password").value).catch(e=>alert(e.message)); }
  function logout() { auth.signOut().then(()=>location.reload()); }
  function loginGoogle() { auth.signInWithRedirect(new firebase.auth.GoogleAuthProvider()); }

  auth.onAuthStateChanged(user => {
    if(user){
      document.getElementById("dashboard").classList.remove("hidden");
      document.getElementById("login-card").classList.add("hidden");
      document.getElementById("menu-btn").style.display="flex";
      document.getElementById("ai-button").style.display="flex";
      document.getElementById("u-name").innerText = user.displayName || "Santri";
      document.getElementById("u-email").innerText = user.email;
    } else {
      document.getElementById("login-card").classList.remove("hidden");
      document.getElementById("dashboard").classList.add("hidden");
    }
  });
</script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(silent=True)
        if not data or 'pesan' not in data:
            return jsonify({"jawaban": "Gagal menerima pesan."}), 400
        pesan_user = data.get('pesan')
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text if response.text else "AI tidak memberikan jawaban."})
    except Exception as e:
        return jsonify({"jawaban": f"Sistem Sibuk: {str(e)}"}), 500

app = app

