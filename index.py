import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Kode ini rahasia, dia akan lapor ke Vercel untuk minta kunci
client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(force=True, silent=True)
        pesan_user = data.get('pesan', '')
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=pesan_user
        )
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Server sibuk, coba lagi ya. ({str(e)})"}), 500

@app.route('/')
def home():
    return "Server AI E-Santri Aktif"
