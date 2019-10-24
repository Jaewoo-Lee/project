/* eslint-disable no-console */
import { register } from 'register-service-worker'
import store from './store'
import firebase from 'firebase/app'
import 'firebase/messaging'
//import controller from '@/services/Controller'

const applicationServerPublicKey = 'BGDkuDHGT0Wa6qnkziHtQnUUbqI53fZyiLc8u4r_ibYIsbMRA0ZcaKjMeHnEn1FGunqirX3L28yTtIpEo9WPx08';
//const vueapp = document.querySelector('#loadingpage');

//const pushButton = document.querySelector('.js-push-btn');

let isSubscribed = false;
let swRegistration = null;
let fcmToken = null;

function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

function subscribeUser() {
  const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
  swRegistration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: applicationServerKey
  })
  .then(function(subscription) {
    console.log('User is subscribed.');

    //updateSubscriptionOnServer(subscription);
    console.log(subscription)
    isSubscribed = true;
  })
  .catch(function(err) {
    console.log('Failed to subscribe the user: ', err);
  });
}

function unsubscribeUser() {
  swRegistration.pushManager.getSubscription()
  .then(function(subscription) {
    if (subscription) {
      //console.log("여기는 구독 해제2")
      //console.log(window.indexedDB)
      return subscription.unsubscribe();
    }
  })
  .catch(function(error) {
    console.log('Error unsubscribing', error);
  })
  .then(function() {
    //updateSubscriptionOnServer(null);

    console.log('User is unsubscribed.');
    isSubscribed = false;
  });
}


function initializeUI() {
  swRegistration.pushManager.getSubscription()
  .then(function(subscription){
    if(subscription===null){
      window.addEventListener('load', function() {
        //pushButton.disabled = true;
        if (isSubscribed) {
          //console.log("여기는 구독 해제2")
          unsubscribeUser();
        } else {
          subscribeUser();
          //console.log("여기가 들어오는데 왜안될까")
        }
      });
    }
  })
  
  // Set the initial subscription value
  swRegistration.pushManager.getSubscription()
  .then(function(subscription) {
    isSubscribed = !(subscription === null);
    
    //updateSubscriptionOnServer(subscription);

    if (isSubscribed) {
      console.log('User IS subscribed.');
      console.log(subscription);
    } else {
      console.log('User is NOT subscribed.');
    }
  });
}


if ('serviceWorker' in navigator){
  console.log('SW found');
  if('PushManager' in window) {
    console.log('Service Worker and Push is supported');

    navigator.serviceWorker.register('/service-worker.js')
    .then(function(swReg) {
      console.log('Service Worker is registered', swReg);

      swRegistration = swReg;
      initializeUI();
    })
    .catch(function(error) {
      console.error('Service Worker Error', error);
    });
  }
  else{
    console.log('PM not found');
  }
} else {
  console.warn('SW is not supported');
  //pushButton.textContent = 'Push Not Supported';
}
