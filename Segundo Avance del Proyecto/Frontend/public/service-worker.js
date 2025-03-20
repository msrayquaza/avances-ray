const shellCache = 'shell-cache-v4'; // Cambia el nombre del caché para forzar actualización
const dynamicCache = 'dynamic-cache-v4';

const shellAssets = [
    '/',
    '/index.html',
    '/login.html',
    '/dashboard.html',
    '/usuarios.html',
    '/styles/global.css',
    '/styles/login.css',
    '/styles/navbarSidebar.css',
    '/src/main.js',
    '/src/api/auth.js',
    '/src/api/usuarios.js',
    '/src/api/session.js',
    '/src/components/navbar.js',
    '/src/components/sidebar.js',
    '/img/logo.png',
    '/img/default-profile.jpg',
    '/manifest.json',
    '/fallback.html'
];

self.addEventListener('install', event => {
    console.log('🛠️ Instalando Service Worker...');
    event.waitUntil(
        caches.open(shellCache)
            .then(cache => {
                console.log('📦 Cacheando assets esenciales...');
                return cache.addAll(shellAssets);
            })
            .catch(error => console.error('❌ Error al cachear en instalación:', error))
    );
});

self.addEventListener('activate', event => {
    console.log('✅ Service Worker activado.');
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys
                    .filter(key => key !== shellCache && key !== dynamicCache)
                    .map(key => {
                        console.log(`🗑️ Eliminando caché viejo: ${key}`);
                        return caches.delete(key);
                    })
            );
        })
    );
});

self.addEventListener('fetch', event => {
    const requestUrl = new URL(event.request.url);
    if (requestUrl.origin.includes('127.0.0.1:8000') && requestUrl.pathname.startsWith('/api/')) {
        console.log('⏭️ Saltando cache para API:', event.request.url);
        return;
    }

    event.respondWith(
        fetch(event.request)
            .then(response => {
                return response;
            })
            .catch(() => {
                console.warn('⚠️ Sin conexión, sirviendo fallback.');
                return caches.match(event.request) || caches.match('/fallback.html');
            })
    );
});
