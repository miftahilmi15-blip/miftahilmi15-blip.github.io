from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Konfigurasi API
genai.configure(api_key="AIzaSyCZmCTKtlYKcte4ytLmqhQbvZy7O3k5Ar4")
model = genai.GenerativeModel('gemini-1.5-flash')

# Ambil HTML dari file luar atau variabel
HTML_CODE = """
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/proses', methods=['POST'])
def proses():
    try:
        data = request.get_json()
        pesan = data.get('pesan', 'Halo')
        
        # Proses AI
        response = model.generate_content(pesan)
        return jsonify({"jawaban": response.text})
    except Exception as e:
        # Log error ke Vercel agar bisa kita baca
        print(f"Error: {str(e)}")
        return jsonify({"jawaban": "Maaf Kak, sistem sedang penuh. Coba sebentar lagi ya."})

app = app() => location.reload()); }
        auth.onAuthStateChanged(user => {
            if (user) {
                document.getElementById('login').classList.add("hidden");
                document.getElementById('dash').classList.remove("hidden");
                menuBtn.style.display = aiBtn.style.display = "flex";
                document.getElementById('uName').innerText = user.displayName || "Santri";
                document.getElementById('uEmail').innerText = user.email;
                if (user.photoURL) document.getElementById('uImg').src = user.photoURL;
            }
        });
        async function sendAI() {
            const input = document.getElementById('aiInput'), chat = document.getElementById('chat'), text = input.value.trim();
            if (!text) return;
            chat.innerHTML += `<div class="msg-user">${text}</div>`;
            input.value = "";
            const loadId = "load-" + Date.now();
            chat.innerHTML += `<div class="msg-ai" id="${loadId}">...</div>`;
            chat.scrollTop = chat.scrollHeight;
            try {
                const res = await fetch("/proses", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ pesan: text }) });
                const data = await res.json();
                document.getElementById(loadId).innerText = data.jawaban;
            } catch { document.getElementById(loadId).innerText = "Error koneksi."; }
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
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
        user_message = data.get('pesan', '')
        
        # Panggil AI dengan penanganan error internal
        response = model.generate_content(f"Jawablah sebagai asisten santri yang ramah: {user_message}")
        
        return jsonify({"jawaban": response.text})
    except Exception as e:
        # Kembalikan pesan error santun jika AI gagal, tapi server tidak crash
        return jsonify({"jawaban": f"Afwan, ada gangguan teknis kecil: {str(e)}"})

# Wajib untuk Vercel
app = appcation.reload()); }
        auth.onAuthStateChanged(user => {
            if (user) {
                document.getElementById('login').classList.add("hidden");
                document.getElementById('dash').classList.remove("hidden");
                menuBtn.style.display = aiBtn.style.display = "flex";
                document.getElementById('uName').innerText = user.displayName || "Santri";
                document.getElementById('uEmail').innerText = user.email;
                if (user.photoURL) document.getElementById('uImg').src = user.photoURL;
            }
        });
        async function sendAI() {
            const input = document.getElementById('aiInput'), chat = document.getElementById('chat'), text = input.value.trim();
            if (!text) return;
            chat.innerHTML += `<div class="msg-user">${text}</div>`;
            input.value = "";
            const loadId = "load-" + Date.now();
            chat.innerHTML += `<div class="msg-ai" id="${loadId}">...</div>`;
            chat.scrollTop = chat.scrollHeight;
            try {
                const res = await fetch("/proses", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ pesan: text }) });
                const data = await res.json();
                document.getElementById(loadId).innerText = data.jawaban;
            } catch { document.getElementById(loadId).innerText = "Error koneksi."; }
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
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
        p = data.get('pesan', '')
        # Memaksa versi API v1 untuk menghindari error 404 v1beta
        response = model.generate_content(
            f"Jawablah sebagai asisten santri yang ramah: {p}",
            transport="rest"
        )
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Maaf, AI sedang istirahat. ({str(e)})"})

# Nama variabel aplikasi untuk Vercel
app = app.com",
            projectId: "e-santri-b62be"
        };
        firebase.initializeApp(firebaseConfig);
        const auth = firebase.auth();

        const menuBtn = document.getElementById('menuBtn');
        const sidebar = document.getElementById('sidebar');
        const closeBtn = document.getElementById('closeBtn');
        const aiBox = document.getElementById('ai-box');
        const aiBtn = document.getElementById('ai-btn');

        menuBtn.onclick = () => sidebar.classList.add("open");
        closeBtn.onclick = () => sidebar.classList.remove("open");
        function toggleAI() { aiBox.style.display = (aiBox.style.display === "flex") ? "none" : "flex"; }

        function login() {
            auth.signInWithEmailAndPassword(document.getElementById('email').value, document.getElementById('password').value).catch(e => alert(e.message));
        }
        function loginGoogle() { auth.signInWithPopup(new firebase.auth.GoogleAuthProvider()); }
        function logout() { auth.signOut().then(() => location.reload()); }

        auth.onAuthStateChanged(user => {
            if (user) {
                document.getElementById('login').classList.add("hidden");
                document.getElementById('dash').classList.remove("hidden");
                menuBtn.style.display = aiBtn.style.display = "flex";
                document.getElementById('uName').innerText = user.displayName || "Santri";
                document.getElementById('uEmail').innerText = user.email;
                if (user.photoURL) document.getElementById('uImg').src = user.photoURL;
            }
        });

        async function sendAI() {
            const input = document.getElementById('aiInput');
            const chat = document.getElementById('chat');
            const text = input.value.trim();
            if (!text) return;

            chat.innerHTML += `<div class="msg-user">${text}</div>`;
            input.value = "";
            const loadId = "load-" + Date.now();
            chat.innerHTML += `<div class="msg-ai" id="${loadId}">...</div>`;
            chat.scrollTop = chat.scrollHeight;

            try {
                const res = await fetch("/proses", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ pesan: text })
                });
                const data = await res.json();
                document.getElementById(loadId).innerText = data.jawaban;
            } catch {
                document.getElementById(loadId).innerText = "Error koneksi.";
            }
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
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
        p = data.get('pesan', '')
        response = model.generate_content(f"Jawablah sebagai asisten santri yang ramah: {p}")
        return jsonify({"jawaban": response.text})
    except Exception as e:
        return jsonify({"jawaban": f"Maaf, AI sedang istirahat. ({str(e)})"})

# Wajib untuk Vercel
app = app






