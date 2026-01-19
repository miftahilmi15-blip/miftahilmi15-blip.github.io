from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # Penting agar index.html diizinkan memanggil Python ini

# --- CONFIG AI ---
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(silent=True)
        if not data or 'pesan' not in data:
            return jsonify({"jawaban": "Pesan tidak terbaca."}), 400
            
        pesan_user = data.get('pesan')
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Sistem Sibuk: {str(e)}"}), 500

app = app
