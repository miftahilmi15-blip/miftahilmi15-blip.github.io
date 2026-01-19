from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# --- CONFIG AI ---
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

# Gunakan r''' agar simbol { } di CSS/JS tidak bentrok dengan f-string Python
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
        # Cek apakah data masuk
        data = request.get_json(silent=True)
        if not data or 'pesan' not in data:
            return jsonify({"jawaban": "Gagal menerima pesan. Pastikan format JSON benar."}), 400
            
        pesan_user = data.get('pesan')
        
        # Panggil AI Gemini
        response = model.generate_content(pesan_user)
        
        if response and response.text:
            return jsonify({"jawaban": response.text})
        else:
            return jsonify({"jawaban": "AI memberikan respon kosong."})

    except Exception as e:
        # Menampilkan pesan error asli agar mudah diperbaiki
        return jsonify({"jawaban": f"Sistem Sibuk (Detail Error: {str(e)})"}), 500

app = app
