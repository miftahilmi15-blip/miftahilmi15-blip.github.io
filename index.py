from flask import Flask, render_template_string, request, jsonify
from google import genai

app = Flask(__name__)

# --- CONFIG AI (Versi Terbaru) ---
client = genai.Client(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")

# Gunakan r''' agar simbol { } di CSS/JS Kakak tidak merusak Python
HTML_CODE = r'''
<!doctype html>
<html lang="id">
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/proses', methods=['POST'])
def proses():
    try:
        # Mengambil data dengan lebih aman
        data = request.get_json(silent=True) or {}
        pesan_user = data.get('pesan', '')

        if not pesan_user:
            return jsonify({"jawaban": "Pesan kosong, silakan ketik sesuatu."})

        # Panggil AI Gemini
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Jawablah sebagai asisten santri yang ramah: {pesan_user}"
        )
        
        return jsonify({"jawaban": response.text})

    except Exception as e:
        # Jika error, tampilkan detailnya agar kita bisa perbaiki lagi
        return jsonify({"jawaban": f"Afwan, sistem sedang sinkronisasi. (Detail: {str(e)})"})

app = app
