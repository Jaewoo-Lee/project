/**
 * Welcome to your Workbox-powered service worker!
 *
 * You'll need to register this file in your web app and you should
 * disable HTTP caching for this file too.
 * See https://goo.gl/nhQhGp
 *
 * The rest of the code is auto-generated. Please don't update this file
 * directly; instead, make changes to your Workbox build configuration
 * and re-run your build process.
 * See https://goo.gl/2aRDsh
 */

importScripts("https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js");

const version = "0.6.25";
const CACHE_NAME = `cache_${version}`;
const FILES_TO_CACHE = [
  '/',
  '/index.html',
  '/new_favicon2.ico',
  '/manifest.json',
  '/img/icons/icon_192.png',
  '/img/icons/icon_512.png',
  '/img/icons/msapplication-icon-144x144.png',

  '/static/css/app.d5e2f9c64f79e833e5397fe5a3196694.css',	// 바뀜

  '/static/fonts/fontawesome-webfont.674f50d.eot',
  '/static/fonts/fontawesome-webfont.af7ae50.woff2',
  '/static/fonts/fontawesome-webfont.b06871f.ttf',
  '/static/fonts/fontawesome-webfont.fee66e7.woff',
  '/static/fonts/weathericons-regular-webfont.2ca3df0.ttf',
  '/static/fonts/weathericons-regular-webfont.e7ef2b4.eot',
  '/static/fonts/weathericons-regular-webfont.f5b0d0d.woff',

  '/static/img/fontawesome-webfont.912ec66.svg',
  '/static/img/noimage2.598991c.png',
  '/static/img/profile.3198a28.png',
  '/static/img/profile2.cfe285c.png',
  '/static/img/weathericons-regular-webfont.b2233bc.svg',

  '/static/js/app.43d680245ee7a223354f.js',
  '/static/js/manifest.2ae2e69a05c33dfc65f8.js',
  '/static/js/vendor.8e594fc9d36eb89daaab.js',
  
  'http://70.12.247.54:8080/searchAllPortfolio.do',
  'http://70.12.247.54:8080/searchAllPost.do'

];

// CODELAB: Precache static resources here.

self.addEventListener('install', function(e) {
  console.log('[Service Worker] Install');
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Pre-caching offline page');
      return cache.addAll(FILES_TO_CACHE)
                  .then(() => self.skipWaiting());
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(CACHE_NAME)
      .then(cache => cache.match(event.request, {ignoreSearch: true}))
      .then(response => {
        return response || fetch(event.request);
      })
  );
});

self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});