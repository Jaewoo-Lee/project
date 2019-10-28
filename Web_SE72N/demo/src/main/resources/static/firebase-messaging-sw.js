importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-messaging.js');
//importScripts('/demo/frontend/src/store.js');
//import store from '../../demo/frontend/src/store'
// Get Instance ID token. Initially this makes a network call, once retrieved
// subsequent calls to getToken will return from cache.
//self.store = require('/demo/frontend/src/store.js').store;
const config = {
	projectId: 'webmobile-sub2-693e3',
	authDomain: 'webmobile-sub2-693e3.firebaseapp.com',
	apiKey: 'AIzaSyDlpBzQlxB2X8oVQ2GRiDmUBV_k7-RO24A',
	databaseURL: 'https://webmobile-sub2-693e3.firebaseio.com',
	storageBucket: '',
	messagingSenderId: "99987372530",
}
firebase.initializeApp(config)
const messaging = firebase.messaging();
//console.log("session:"+ clients.window)
messaging.setBackgroundMessageHandler(function(payload){
    const title = payload.notification.title;
    const options = {
      body: payload.notification.body,
      click_action:payload.notification.click_action,
      data:{
        "click_action":payload.notification.click_action
      }
    };
    return self.registration.showNotification(title,options);
});



self.addEventListener('notificationclick', function(event) {
	  console.log('[Service Worker] Notification click Received.');
	  event.notification.close();
	  console.log(event.notification)
	  event.waitUntil(
	    clients.openWindow(event.notification.data.click_action)
	  );
	});