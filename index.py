from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- KONFIGURASI AI ---
# Gunakan API Key Kakak
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- TEMPLATE HTML ---
# Pastikan HTML Kakak ada di dalam tanda kutip tiga ini
HTML_CODE = """
<!doctype html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
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
        pesan_user = data.get('pesan', 'Halo')
        
        # Panggil AI
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Afwan, sistem sedang sinkronisasi. ({str(e)})"})

# Pastikan baris terakhir HANYA SEPERTI INI
app = app
