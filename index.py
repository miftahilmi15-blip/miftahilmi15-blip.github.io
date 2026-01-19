from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Konfigurasi AI
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

# Masukkan kode HTML v16 Kakak di dalam tanda kutip ini
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
        pesan = data.get('pesan', '')
        response = model.generate_content(pesan)
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Error: {str(e)}"})

# HANYA INI, JANGAN ADA JAVASCRIPT DI BAWAH SINI
app = app
