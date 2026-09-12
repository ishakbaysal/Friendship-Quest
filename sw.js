
const CACHE = 'yds-v1';
self.addEventListener('install', e => {
    e.waitUntil(
        caches.open(CACHE).then(c => c.addAll(['./index.html']))
    );
    self.skipWaiting();
});
self.addEventListener('activate', e => {
    e.waitUntil(self.clients.claim());
});
self.addEventListener('fetch', e => {
    e.respondWith(
        caches.match(e.request).then(r => r || fetch(e.request))
    );
});
// Arka planda canlı tut
self.addEventListener('message', e => {
    if (e.data === 'keepalive') {
        console.log('SW canlı:', new Date().toLocaleTimeString());
    }
});
