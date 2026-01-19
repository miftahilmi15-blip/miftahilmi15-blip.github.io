from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- KONFIGURASI GOOGLE GEMINI AI ---
# Menggunakan API Key yang kamu miliki
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")

# Inisialisasi model dengan versi yang paling stabil untuk menghindari error 404
model = genai.GenerativeModel('gemini-1.5-flash')

# --- KODE HTML DASHBOARD PRO ---
# Kode HTML yang kamu berikan disisipkan ke dalam variabel ini
HTML_CODE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>E-Santri | Pro</title>

    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Noto+Naskh+Arabic:wght@700&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

    <style>
        :root {
            --primary: #1f6f51;
            --grad: linear-gradient(135deg, #1f6f51, #2ecc71);
            --bg: #f8faf9;
            --shadow: 0 10px 30px rgba(31, 111, 81, .12);
        }

        * { box-sizing: border-box; font-family: 'Poppins', sans-serif; -webkit-tap-highlight-color: transparent; }
        body { margin: 0; background: var(--bg); color: #2d3436; overflow-x: hidden; }

        .hidden { display: none !important; }

        .container { max-width: 420px; margin: auto; padding: 20px; min-height: 100vh; }
        .header { text-align: center; padding: 25px 0; }
        .header h1 { font-family: 'Montserrat', sans-serif; font-size: 32px; font-weight: 900; color: var(--primary); margin: 0; }

        .menu-btn {
            position: fixed; top: 22px; right: 22px; z-index: 2100;
            width: 48px; height: 48px; border-radius: 14px;
            background: #fff; color: var(--primary);
            display: none; align-items: center; justify-content: center;
            box-shadow: var(--shadow); cursor: pointer;
        }

        .sidebar {
            position: fixed; inset: 0; background: rgba(255, 255, 255, .98);
            z-index: 2000; transform: translateX(100%);
            transition: .4s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex; flex-direction: column; align-items: center; justify-content: center;
        }
        .sidebar.open { transform: translateX(0); }
        .close { position: absolute; top: 25px; right: 25px; font-size: 28px; cursor: pointer; color: #aaa; }
        
        .profile { text-align: center; margin-bottom: 35px; }
        .profile img { width: 90px; height: 90px; border-radius: 25px; box-shadow: var(--shadow); object-fit: cover; }
        
        .nav { width: 100%; max-width: 280px; display: flex; flex-direction: column; gap: 14px; }
        .nav a {
            padding: 15px; border-radius: 18px; text-decoration: none;
            background: #fff; color: #333; font-weight: 600;
            display: flex; gap: 10px; align-items: center; justify-content: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, .04); transition: .2s;
        }

        .card { background: #fff; padding: 35px 30px; border-radius: 35px; box-shadow: var(--shadow); }
        input {
            width: 100%; padding: 15px; border-radius: 14px;
            border: 1px solid #eee; margin-bottom: 14px; outline: none; font-size: 14px;
        }
        .btn { 
            width: 100%; padding: 16px; border: none; border-radius: 16px; 
            background: var(--grad); color: #fff; font-weight: 700; cursor: pointer; 
        }
        .btn-google {
            margin-top: 20px; border: 1.5px solid #eee; background: #fff;
            display: flex; gap: 12px; align-items: center; justify-content: center;
            font-weight: 700; border-radius: 16px; padding: 14px; cursor: pointer;
        }
        .btn-google img { width: 22px; }

        .streak {
            background: var(--grad); border-radius: 24px; padding: 20px;
            color: #fff; display: flex; justify-content: space-between; align-items: center;
            box-shadow: 0 15px 35px rgba(31, 111, 81, .25);
        }
        .fire { font-size: 38px; }
        .fire.off { filter: grayscale(1) opacity(.4); transform: scale(.85); }

        .mah {
            background: #fff; border-radius: 50px; padding: 14px 18px;
            margin: 22px 0; box-shadow: var(--shadow);
            display: flex; align-items: center; overflow: hidden;
        }
        .label { 
            background: #d4b96a; color: #fff; font-size: 10px;
            padding: 5px 12px; border-radius: 50px; margin-right: 12px; font-weight: 800; white-space: nowrap;
        }

        .menu { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
        .item {
            background: #fff; border-radius: 24px; padding: 20px 10px;
            text-align: center; box-shadow: var(--shadow);
            cursor: pointer; transition: .2s;
        }
        .item i { font-size: 24px; color: var(--primary); margin-bottom: 8px; display: block; }
        .item span { display: block; font-size: 11px; font-weight: 700; color: #555; }

        #ai-btn {
            position: fixed; bottom: 20px; right: 20px; z-index: 1200;
            width: 60px; height: 60px; border-radius: 50%;
            background: #15803d; color: #fff;
            display: none; align-items: center; justify-content: center;
            font-size: 24px; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        #ai-box {
            position: fixed; bottom: 90px; right: 20px; width: 300px; max-height: 400px;
            background: #fff; border-radius: 16px; box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            display: none; flex-direction: column; overflow: hidden; z-index: 1200;
        }
        .chat-content { flex: 1; padding: 15px; overflow-y: auto; font-size: 13px; display: flex; flex-direction: column; }
        .msg-ai { background: #f1f1f1; padding: 10px; border-radius: 12px 12px 12px 0; margin-bottom: 10px; align-self: flex-start; max-width: 85%; }
        .msg-user { background: var(--primary); color: #fff; padding: 10px; border-radius: 12px 12px 0 12px; margin-bottom: 10px; align-self: flex-end; max-width: 85%; }
    </style>
</head>
<body>

    <div class="menu-btn" id="menuBtn"><i class="fa fa-bars"></i></div>

    <div class="sidebar" id="sidebar">
        <div class="close" id="closeBtn">✕</div>
        <div class="profile">
            <img id="uImg" src="https://ui-avatars.com/api/?background=1f6f51&color=fff&name=Santri" alt="User">
            <h3 id="uName">Santri</h3>
            <p id="uEmail" style="font-size:12px;color:#888"></p>
        </div>
        <div class="nav">
            <a href="#" onclick="location.reload()">Dashboard</a>
            <a href="#" onclick="logout()" style="color:#e74c3c">Keluar</a>
        </div>
    </div>

    <main class="container">
        <div class="header"><h1>E-SANTRI</h1></div>

        <section id="login" class="card">
            <input id="email" type="email" placeholder="Email">
            <input id="password" type="password" placeholder="Password">
            <button class="btn" onclick="login()">MASUK</button>
            <div style="margin:20px 0;color:#ccc;text-align:center;font-size: 12px;">— ATAU —</div>
            <div class="btn-google" onclick="loginGoogle()">
                <img src="https://www.gstatic.com/images/branding/product/1x/gsa_512dp.png" alt="Google">
                Masuk dengan Google
            </div>
        </section>

        <section id="dash" class="hidden">
            <div class="streak">
                <div><small style="opacity: 0.8;">Status Absensi</small><h2 id="streakText" style="margin: 5px 0 0 0;">Ketuk Absensi</h2></div>
                <div id="fire" class="fire off">🔥</div>
            </div>

            <div class="mah">
                <div class="label">MAHFUZAT</div>
                <marquee id="mahText" scrollamount="4">Memuat hikmah...</marquee>
            </div>

            <div class="menu">
                <div class="item"><i class="fa fa-book-quran"></i><span>Al-Qur’an</span></div>
                <div class="item"><i class="fa fa-calendar-check"></i><span>Absensi</span></div>
                <div class="item"><i class="fa fa-star"></i><span>Tahfidz</span></div>
                <div class="item"><i class="fa fa-language"></i><span>Kamus</span></div>
                <div class="item"><i class="fa fa-book"></i><span>Perpus</span></div>
                <div class="item"><i class="fa fa-mosque"></i><span>Budaya</span></div>
            </div>
        </section>
    </main>

    <div id="ai-btn" onclick="toggleAI()">🌙</div>
    <div id="ai-box">
        <div style="background:#15803d;color:#fff;padding:12px;text-align:center;font-weight:bold">Asisten E-Santri</div>
        <div id="chat" class="chat-content">
            <div class="msg-ai">Assalamu’alaikum 😊 Ada yang bisa dibantu?</div>
        </div>
        <div style="display:flex;padding:10px;border-top:1px solid #eee">
            <input id="aiInput" placeholder="Tanya..." style="flex:1;border:none;outline:none;margin-bottom:0">
            <button onclick="sendAI()" style="border:none;background:none;color:#15803d;font-weight:700;padding-left:10px">Kirim</button>
        </div>
    </div>

    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-auth-compat.js"></script>

    <script>
        const firebaseConfig = {
            apiKey: "AIzaSyCFVjE7ey5g__Iv4vUOZftB7g8GtSTSsEo",
            authDomain: "e-santri-b62be.firebaseapp.com",
            projectId: "e-santri-b62be"
        };
        firebase.initializeApp(firebaseConfig);
        const auth = firebase.auth();

        const menuBtn = document.getElementById('menuBtn');
        const sidebar = document.getElementById('sidebar');
        const closeBtn = document.getElementById('closeBtn');
        const aiBox = document.getElementById('ai-box');
        const aiBtn = document.getElementById('ai-btn');

        menuBtn.onclick = () => sidebar.classList.add("open");
        closeBtn.onclick = () => sidebar.classList.remove("open");
        function toggleAI() { aiBox.style.display = (aiBox.style.display === "flex") ? "none" : "flex"; }

        function login() {
            auth.signInWithEmailAndPassword(document.getElementById('email').value, document.getElementById('password').value).catch(e => alert(e.message));
        }
        function loginGoogle() { auth.signInWithPopup(new firebase.auth.GoogleAuthProvider()); }
        function logout() { auth.signOut().then(() => location.reload()); }

        auth.onAuthStateChanged(user => {
            if (user) {
                document.getElementById('login').classList.add("hidden");
                document.getElementById('dash').classList.remove("hidden");
                menuBtn.style.display = aiBtn.style.display = "flex";
                document.getElementById('uName').innerText = user.displayName || "Santri";
                document.getElementById('uEmail').innerText = user.email;
                if (user.photoURL) document.getElementById('uImg').src = user.photoURL;
            }
        });

        async function sendAI() {
            const input = document.getElementById('aiInput');
            const chat = document.getElementById('chat');
            const text = input.value.trim();
            if (!text) return;

            chat.innerHTML += `<div class="msg-user">${text}</div>`;
            input.value = "";
            const loadId = "load-" + Date.now();
            chat.innerHTML += `<div class="msg-ai" id="${loadId}">...</div>`;
            chat.scrollTop = chat.scrollHeight;

            try {
                const res = await fetch("/proses", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ pesan: text })
                });
                const data = await res.json();
                document.getElementById(loadId).innerText = data.jawaban;
            } catch {
                document.getElementById(loadId).innerText = "Error koneksi.";
            }
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json()
        p = data.get('pesan', '')
        response = model.generate_content(f"Jawablah sebagai asisten santri yang ramah: {p}")
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Maaf, AI sedang istirahat. ({str(e)})"})

# Wajib untuk Vercel
app = app

