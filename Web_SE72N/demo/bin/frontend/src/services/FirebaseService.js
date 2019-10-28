import firebase from 'firebase/app'
import 'firebase/firestore'
import 'firebase/auth'
import 'firebase/messaging'
import controller from '@/services/Controller'

// Setup Firebase
const config = {
	projectId: 'webmobile-sub2-693e3',
	authDomain: 'webmobile-sub2-693e3.firebaseapp.com',
	apiKey: 'AIzaSyDlpBzQlxB2X8oVQ2GRiDmUBV_k7-RO24A',
	databaseURL: 'https://webmobile-sub2-693e3.firebaseio.com',
	storageBucket: '',
	messagingSenderId: "99987372530",
}

firebase.initializeApp(config)
const messaging = firebase.messaging()

export default {
	name: 'FirebaseService',
	pushMessaging() {
		messaging.requestPermission()
		.then(function() {
			console.log('Have Permission')
			return messaging.getToken()
		})
		.then(function(token) {
			// 이 토큰을 데이터베이스에 저장한다
			var temp = controller.saveToken(token)
			console.log(token)
			console.log(temp)
		})
		.catch(function(err) {
			console.log('Error Occured')
		})

		messaging.onMessage(function(payload) {
			console.log('onMessage: ', payload)
			const title = payload.notification.title;
			const options = {
			  body: payload.notification.body,
			  click_action:payload.notification.click_action,
			  data:{
				  "click_action":payload.notification.click_action
			  }
			};
			var notification = new Notification(title, options);
			notification.onclick = function(event) {
				event.preventDefault(); // prevent the browser from focusing the Notification's tab
				console.log(options.click_action)
				window.open(options.click_action, '_blank');
			  }
		})
	},
	loginWithFacebook() {
		let provider = new firebase.auth.FacebookAuthProvider()
		return firebase.auth().signInWithPopup(provider).then(function(result) {
			let accessToken = result.credential.accessToken
			let user = result.user
			return result
			/*
			user.displayName : 유저이름
			usesr.email : 유저이메일
			*/
		}).catch(function(error) {
			console.error('[Facebook Login Error]', error)
		})
	},
		logoutFacebook() {
		firebase.auth().signOut().then(function() {
			console.log('[Facebook Logout]')
		}).catch(function(error) {
			return error
		})
	},
	
}
