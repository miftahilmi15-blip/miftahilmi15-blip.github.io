from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Konfigurasi AI
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(force=True, silent=True)
        pesan_user = data.get('pesan', '')
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Maaf, sedang ada kendala: {str(e)}"}), 500

app = app
