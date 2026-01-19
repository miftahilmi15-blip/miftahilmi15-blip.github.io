from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- CONFIG AI ---
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- HTML CODE ---
# Masukkan seluruh kode HTML v16 Anda di antara tanda kutip tiga di bawah
HTML_CODE = """
<!doctype html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <title>E-Santri | Pro v16</title>
    </head>
<body>
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
        pesan_user = data.get('pesan', '')
        
        # Panggil Gemini AI
        response = model.generate_content(pesan_user)
        
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Afwan, ada kendala teknis: {str(e)}"})

# BARIS INI HARUS BERSIH, JANGAN ADA JS DI BAWAHNYA
app = app
