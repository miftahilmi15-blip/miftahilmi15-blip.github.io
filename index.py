from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # Mengizinkan index.html memanggil file ini

# --- CONFIG AI ---
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(silent=True)
        if not data or 'pesan' not in data:
            return jsonify({"jawaban": "Gagal menerima pesan."}), 400
            
        pesan_user = data.get('pesan')
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Sistem Sibuk: {str(e)}"}), 500

# Wajib ada agar Vercel mengenali app
app = app     document.getElementById(loadingId).innerText = "Afwan, asisten sedang sinkronisasi.";
    }
    box.scrollTop = box.scrollHeight;
  }

  function login() { auth.signInWithEmailAndPassword(document.getElementById("email").value, document.getElementById("password").value).catch(e=>alert(e.message)); }
  function logout() { auth.signOut().then(()=>location.reload()); }
  function loginGoogle() { auth.signInWithRedirect(new firebase.auth.GoogleAuthProvider()); }

  auth.onAuthStateChanged(user => {
    if(user){
      document.getElementById("dashboard").classList.remove("hidden");
      document.getElementById("login-card").classList.add("hidden");
      document.getElementById("menu-btn").style.display="flex";
      document.getElementById("ai-button").style.display="flex";
      document.getElementById("u-name").innerText = user.displayName || "Santri";
      document.getElementById("u-email").innerText = user.email;
    } else {
      document.getElementById("login-card").classList.remove("hidden");
      document.getElementById("dashboard").classList.add("hidden");
    }
  });
</script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(silent=True, force=True)
        if not data or 'pesan' not in data:
            return jsonify({"jawaban": "Gagal menerima pesan."}), 400
        pesan_user = data.get('pesan')
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text if response.text else "AI tidak memberikan jawaban."})
    except Exception as e:
        return jsonify({"jawaban": f"Sistem Sibuk: {str(e)}"}), 500

app = app.getElementById(loadingId).innerText = "Afwan, asisten sedang sinkronisasi.";
    }
    box.scrollTop = box.scrollHeight;
  }

  function login() { auth.signInWithEmailAndPassword(document.getElementById("email").value, document.getElementById("password").value).catch(e=>alert(e.message)); }
  function logout() { auth.signOut().then(()=>location.reload()); }
  function loginGoogle() { auth.signInWithRedirect(new firebase.auth.GoogleAuthProvider()); }

  auth.onAuthStateChanged(user => {
    if(user){
      document.getElementById("dashboard").classList.remove("hidden");
      document.getElementById("login-card").classList.add("hidden");
      document.getElementById("menu-btn").style.display="flex";
      document.getElementById("ai-button").style.display="flex";
      document.getElementById("u-name").innerText = user.displayName || "Santri";
      document.getElementById("u-email").innerText = user.email;
    } else {
      document.getElementById("login-card").classList.remove("hidden");
      document.getElementById("dashboard").classList.add("hidden");
    }
  });
</script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json(silent=True)
        if not data or 'pesan' not in data:
            return jsonify({"jawaban": "Gagal menerima pesan."}), 400
        pesan_user = data.get('pesan')
        response = model.generate_content(pesan_user)
        return jsonify({"jawaban": response.text if response.text else "AI tidak memberikan jawaban."})
    except Exception as e:
        return jsonify({"jawaban": f"Sistem Sibuk: {str(e)}"}), 500

app = app


