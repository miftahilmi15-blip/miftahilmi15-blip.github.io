from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- CONFIG AI ---
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

# Gunakan r""" agar karakter khusus di HTML tidak merusak Python
HTML_CODE = r"""
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
    try:
        return render_template_string(HTML_CODE)
    except Exception as e:
        return f"Error menampilkan halaman: {str(e)}"

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"jawaban": "Data tidak terkirim"}), 400
        
        user_msg = data.get('pesan', '')
        response = model.generate_content(user_msg)
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Maaf, ada kendala: {str(e)}"}), 500

app = app
