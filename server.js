const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const admin = require('firebase-admin');

// 1. KONEKSI KE FIREBASE (Ganti URL-nya dengan URL database kamu)
const serviceAccount = require("./serviceAccountKey.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://e-santri-b62be-default-rtdb.asia-southeast1.firebasedatabase.app"
});
const db = admin.database();

// 2. SETUP WHATSAPP
const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { args: ['--no-sandbox', '--disable-setuid-sandbox'] }
});

client.on('qr', (qr) => {
    qrcode.generate(qr, {small: true});
    console.log('SCAN QR INI DENGAN WA HP BOS:');
});

client.on('ready', () => {
    console.log('✅ WA GATEWAY SIAP DIGUNAKAN!');
});

// 3. LOGIKA PENGIRIMAN (AMBIL DARI ANTRIAN)
db.ref('antrian_wa').on('child_added', async (snapshot) => {
    const data = snapshot.val();
    const key = snapshot.key;

    try {
        // Kirim Pesan
        await client.sendMessage(data.nomor + "@c.us", data.pesan);
        console.log(`🚀 Terkirim ke: ${data.nomor}`);

        // Hapus dari antrian supaya tidak dikirim berulang
        await db.ref('antrian_wa/' + key).remove();

        // JEDA 10 DETIK (Biar gak kena banned WA)
        await new Promise(resolve => setTimeout(resolve, 10000)); 

    } catch (err) {
        console.error("Gagal kirim ke " + data.nomor, err);
    }
});

client.initialize();
