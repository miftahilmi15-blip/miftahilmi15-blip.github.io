from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Konfigurasi Client AI Terbaru
client = genai.Client(api_key="AIzaSyA2XKM64g3ouFO7sLU1VPTehgnvPrlQ5s8")

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(force=True, silent=True)
        pesan_user = data.get('pesan', '')
        
        # Cara panggil Gemini terbaru 2026
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=pesan_user
        )
        
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Kendala teknis: {str(e)}"}), 500

# Baris ini SANGAT PENTING agar Vercel tidak 404
@app.route('/')
def home():
    return "Server AI E-Santri Aktif"

app = app

