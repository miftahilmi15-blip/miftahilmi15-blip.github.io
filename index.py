from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# API Key
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")

# GANTI BAGIAN KONFIGURASI MODEL DENGAN INI:
try:
# GANTI BAGIAN MODEL DENGAN INI
model = genai.GenerativeModel('gemini-1.0-pro')

HTML_CODE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>E-Santri | Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <style>
        :root { --primary: #1f6f51; --grad: linear-gradient(135deg, #1f6f51, #2ecc71); --bg: #f8faf9; }
        * { box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body { margin: 0; background: var(--bg); color: #2d3436; }
        .hidden { display: none !important; }
        .container { max-width: 420px; margin: auto; padding: 20px; min-height: 100vh; }
        .header { text-align: center; padding: 25px 0; }
        .header h1 { font-family: 'Montserrat', sans-serif; font-size: 32px; color: var(--primary); margin: 0; }
        .card { background: #fff; padding: 30px; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        input { width: 100%; padding: 15px; border-radius: 14px; border: 1px solid #eee; margin-bottom: 14px; outline: none; }
        .btn { width: 100%; padding: 16px; border: none; border-radius: 16px; background: var(--grad); color: #fff; font-weight: 700; cursor: pointer; }
        .streak { background: var(--grad); border-radius: 24px; padding: 20px; color: #fff; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;}
        .menu { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
        .item { background: #fff; border-radius: 20px; padding: 15px 5px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.05); cursor: pointer; }
        .item i { font-size: 22px; color: var(--primary); margin-bottom: 8px; display: block; }
        .item span { font-size: 10px; font-weight: 700; }
        #ai-btn { position: fixed; bottom: 25px; right: 25px; width: 60px; height: 60px; border-radius: 50%; background: #15803d; color: #fff; display: none; align-items: center; justify-content: center; font-size: 24px; cursor: pointer; box-shadow: 0 5px 20px rgba(0,0,0,0.2); z-index: 1000; }
        #ai-box { position: fixed; bottom: 95px; right: 20px; width: 320px; height: 450px; background: #fff; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.2); display: none; flex-direction: column; overflow: hidden; z-index: 1000; border: 1px solid #eee; }
        .chat-header { background: #15803d; color: #fff; padding: 15px; text-align: center; font-weight: bold; }
        .chat-content { flex: 1; padding: 15px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; background: #f9f9f9; }
        .msg { padding: 10px 14px; border-radius: 15px; font-size: 13px; max-width: 85%; line-height: 1.4; }
        .msg-ai { background: #fff; align-self: flex-start; border: 1px solid #eee; color: #333; }
        .msg-user { background: #15803d; color: #fff; align-self: flex-end; }
        .chat-input { display: flex; padding: 10px; background: #fff; border-top: 1px solid #eee; }
        .chat-input input { margin-bottom: 0; border: none; font-size: 13px; }
    </style>
</head>
<body>
    <main class="container">
        <div class="header"><h1>E-SANTRI</h1></div>
        <section id="login" class="card">
            <input id="email" type="email" placeholder="Email Santri">
            <input id="password" type="password" placeholder="Password">
            <button class="btn" onclick="login()">MASUK</button>
        </section>
        <section id="dash" class="hidden">
            <div class="streak">
                <div><small>Status Absensi</small><h2 id="streakText" style="margin:0">Ketuk Absensi</h2></div>
                <div style="font-size:30px">🔥</div>
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
        <div class="chat-header">Asisten E-Santri</div>
        <div id="chat" class="chat-content">
            <div class="msg msg-ai">Assalamu’alaikum! Ada yang bisa saya bantu? 😊</div>
        </div>
        <div class="chat-input">
            <input id="aiInput" placeholder="Tanya sesuatu..." onkeypress="if(event.key==='Enter') sendAI()">
            <button onclick="sendAI()" style="border:none;background:none;color:#15803d;font-weight:bold;cursor:pointer">Kirim</button>
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
        function login() {
            const e = document.getElementById('email').value;
            const p = document.getElementById('password').value;
            auth.signInWithEmailAndPassword(e, p).catch(err => alert(err.message));
        }
        auth.onAuthStateChanged(user => {
            if(user) {
                document.getElementById('login').classList.add('hidden');
                document.getElementById('dash').classList.remove('hidden');
                document.getElementById('ai-btn').style.display = 'flex';
            }
        });
        function toggleAI() {
            const box = document.getElementById('ai-box');
            box.style.display = (box.style.display === 'flex') ? 'none' : 'flex';
        }
        async function sendAI() {
            const input = document.getElementById('aiInput');
            const chat = document.getElementById('chat');
            const val = input.value.trim();
            if(!val) return;
            chat.innerHTML += `<div class="msg msg-user">${val}</div>`;
            input.value = "";
            chat.scrollTop = chat.scrollHeight;
            const loadId = "load-" + Date.now();
            chat.innerHTML += `<div class="msg msg-ai" id="${loadId}">Sedang mengetik...</div>`;
            try {
                const res = await fetch('/proses', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ pesan: val })
                });
                const d = await res.json();
                document.getElementById(loadId).innerText = d.jawaban;
            } catch {
                document.getElementById(loadId).innerText = "Maaf, koneksi terputus.";
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
        # Pastikan prompt dikirim dengan benar ke Gemini
        response = model.generate_content(f"Berperanlah sebagai asisten santri yang ramah. Jawab: {p}")
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Error AI: {str(e)}"})

# Baris ini wajib ada untuk Vercel
app = app


