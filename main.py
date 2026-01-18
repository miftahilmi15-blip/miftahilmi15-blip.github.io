from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# API Key kamu
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")

# --- KODE PINTAR: MENCARI MODEL YANG TERSEDIA ---
try:
    # Google akan kasih daftar model yang akun kamu boleh pakai
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # Kita ambil model pertama yang dia kasih
    model_name = models[0]
    print(f"BERHASIL: Menggunakan model {model_name}")
    model = genai.GenerativeModel(model_name)
except Exception as e:
    print(f"Gagal deteksi otomatis: {e}")
    # Jika gagal deteksi, kita paksa pakai gemini-pro (tanpa embel-embel models/)
    model = genai.GenerativeModel('gemini-pro')

HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>E-Santri AI Pro</title>
    <style>
        body { font-family: sans-serif; background: #f0fdf4; margin: 0; display: flex; flex-direction: column; align-items: center; }
        .header { background: #15803d; color: white; width: 100%; max-width: 400px; padding: 15px; text-align: center; border-radius: 0 0 15px 15px; font-weight: bold; }
        #chatbox { width: 90%; max-width: 400px; height: 400px; overflow-y: auto; background: white; margin-top: 10px; padding: 10px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); display: flex; flex-direction: column; }
        .msg { margin: 10px 0; padding: 12px; border-radius: 15px; font-size: 14px; line-height: 1.5; max-width: 80%; }
        .ai { background: #e8f5e9; align-self: flex-start; color: #1b4332; border-bottom-left-radius: 2px; }
        .user { background: #15803d; color: white; align-self: flex-end; border-bottom-right-radius: 2px; }
        .input-area { width: 90%; max-width: 420px; display: flex; padding: 15px; gap: 8px; box-sizing: border-box; }
        input { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 25px; outline: none; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); }
        button { width: 45px; height: 45px; background: #15803d; color: white; border: none; border-radius: 50%; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">🌙 E-SANTRI AI PRO</div>
    <div id="chatbox">
        <div class="msg ai">Assalamu'alaikum! Ada yang bisa saya bantu terkait pelajaran pesantren hari ini?</div>
    </div>
    <div class="input-area">
        <input type="text" id="text" placeholder="Tanyakan sesuatu...">
        <button onclick="send()">➤</button>
    </div>

    <script>
        async function send() {
            const i = document.getElementById('text');
            const c = document.getElementById('chatbox');
            const val = i.value;
            if(!val) return;
            
            c.innerHTML += `<div class="msg user">${val}</div>`;
            i.value = "";
            c.scrollTop = c.scrollHeight;

            const res = await fetch('/proses', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({pesan: val})
            });
            const d = await res.json();
            c.innerHTML += `<div class="msg ai">${d.jawaban}</div>`;
            c.scrollTop = c.scrollHeight;
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
        data = request.json
        p = data.get('pesan')
        r = model.generate_content(f"Jawablah dengan bahasa santun sebagai asisten pesantren: {p}")
        return jsonify({"jawaban": r.text})
    except Exception as e:
        return jsonify({"jawaban": f"Kendala: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)