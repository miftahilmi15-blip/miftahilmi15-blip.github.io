from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# API Key - Pastikan tidak ada spasi di awal/akhir
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")

# Konfigurasi Model AI
try:
    # Mencoba menggunakan Gemini 1.5 Flash (lebih cepat dan stabil untuk web)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    # Cadangan jika model di atas tidak tersedia
    model = genai.GenerativeModel('gemini-pro')

HTML_CODE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Santri AI Pro</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0fdf4; margin: 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }
        .header { background: #15803d; color: white; width: 100%; max-width: 500px; padding: 20px; text-align: center; border-radius: 0 0 20px 20px; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        #chatbox { width: 95%; max-width: 500px; height: 450px; overflow-y: auto; background: white; margin-top: 15px; padding: 15px; border-radius: 15px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); display: flex; flex-direction: column; box-sizing: border-box; }
        .msg { margin: 8px 0; padding: 12px 16px; border-radius: 18px; font-size: 14px; line-height: 1.5; max-width: 85%; word-wrap: break-word; }
        .ai { background: #f0fdf4; align-self: flex-start; color: #166534; border: 1px solid #dcfce7; border-bottom-left-radius: 2px; }
        .user { background: #15803d; color: white; align-self: flex-end; border-bottom-right-radius: 2px; }
        .input-area { width: 95%; max-width: 500px; display: flex; padding: 20px 0; gap: 10px; }
        input { flex: 1; padding: 12px 20px; border: 2px solid #e2e8f0; border-radius: 30px; outline: none; transition: border 0.3s; }
        input:focus { border-color: #15803d; }
        button { width: 50px; height: 50px; background: #15803d; color: white; border: none; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.3s; }
        button:hover { background: #166534; transform: scale(1.05); }
        .loading { font-style: italic; color: #64748b; font-size: 12px; }
    </style>
</head>
<body>
    <div class="header">🌙 E-SANTRI AI PRO</div>
    <div id="chatbox">
        <div class="msg ai">Assalamu'alaikum! Saya asisten E-Santri. Ada yang bisa saya bantu hari ini?</div>
    </div>
    <div class="input-area">
        <input type="text" id="text" placeholder="Tulis pesan..." autocomplete="off">
        <button onclick="send()">➤</button>
    </div>

    <script>
        const chatbox = document.getElementById('chatbox');
        const input = document.getElementById('text');

        input.addEventListener("keypress", function(event) {
            if (event.key === "Enter") { send(); }
        });

        async function send() {
            const val = input.value.trim();
            if(!val) return;
            
            // Tampilkan pesan user
            chatbox.innerHTML += `<div class="msg user">${val}</div>`;
            input.value = "";
            chatbox.scrollTop = chatbox.scrollHeight;

            // Loading state
            const loadingId = "load-" + Date.now();
            chatbox.innerHTML += `<div class="msg ai" id="${loadingId}"><span class="loading">Sedang berpikir...</span></div>`;
            chatbox.scrollTop = chatbox.scrollHeight;

            try {
                const res = await fetch('/proses', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({pesan: val})
                });
                
                if (!res.ok) throw new Error('Server bermasalah');
                
                const d = await res.json();
                document.getElementById(loadingId).innerText = d.jawaban;
            } catch (e) {
                document.getElementById(loadingId).innerText = "Maaf, koneksi terputus atau server sibuk. Coba lagi ya.";
            }
            chatbox.scrollTop = chatbox.scrollHeight;
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
        pertanyaan = data.get('pesan', '')
        
        if not pertanyaan:
            return jsonify({"jawaban": "Pesan kosong."})

        # Memberikan instruksi tambahan agar AI menjawab seperti asisten pesantren
        prompt = f"Berperanlah sebagai asisten santri yang ramah dan berilmu. Pertanyaan: {pertanyaan}"
        response = model.generate_content(prompt)
        
        return jsonify({"jawaban": response.text})
    except Exception as e:
        print(f"Error: {str(e)}") # Muncul di Logs Vercel
        return jsonify({"jawaban": f"Maaf, sedang ada kendala teknis. (Error: {str(e)})"})

# PENTING UNTUK VERCEL
app = app

if __name__ == '__main__':
    app.run(debug=True)
