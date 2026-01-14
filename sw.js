const CACHE_NAME = 'byond-prayer-v2';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap',
  'https://www.islamcan.com/audio/adhan/makkah.mp3'
];

// 1. Install Service Worker & Simpan Audio Adzan ke Cache
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// 2. Bersihkan Cache Lama jika ada pembaruan
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// 3. Strategi Fetch (Agar aplikasi bisa dibuka tanpa internet)
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

// 4. Menangani interaksi saat notifikasi adzan diklik
self.addEventListener('notificationclick', (event) => {
  event.notification.close(); // Tutup notifikasi saat diklik

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      // Jika aplikasi sudah terbuka, fokuskan ke tab tersebut
      for (const client of clientList) {
        if (client.url === '/' && 'focus' in client) {
          return client.focus();
        }
      }
      // Jika belum terbuka, buka aplikasi
      if (clients.openWindow) {
        return clients.openWindow('./');
      }
    })
  );
});
