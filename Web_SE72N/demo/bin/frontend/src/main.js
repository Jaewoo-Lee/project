import 'es6-promise/auto'

import '@babel/polyfill'
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueSimplemde from 'vue-simplemde'
import 'simplemde/dist/simplemde.min.css'
import 'font-awesome/css/font-awesome.min.css'
import 'weather-icons/css/weather-icons.min.css'
import axios from 'axios'

import router from '@/router'
import store from './store'
import './registerServiceWorker'
import VueResizeText from 'vue-resize-text';
import VueAnalytics from 'vue-analytics'
import App from '@/App'


Vue.prototype.$http = axios
Vue.config.productionTip = false

Vue.use(Vuetify, {
  iconfont: 'fa',
  theme: {
    primary: '#3f51b5',
    secondary: '#b0bec5',
  	accent: '#8c9eff',
  	error: '#b71c1c'
	}
})

Vue.use(VueSimplemde)
Vue.use(VueAnalytics, {
  id: 'UA-145146446-1',
  checkDuplicatedScript: true,
  router,
  autoTracking: {
    screenview: true,
    pageviewOnLoad: false
    // pageviewTemplate (route) {
    //   return {
    //     page: route.path,
    //     title: document.title,
    //     location: window.location.href
    //   }
  }
})

const isLocalhost = Boolean(
  window.location.hostname === 'localhost' ||
  // [::1] is the IPv6 localhost address.
  window.location.hostname === '[::1]' ||
  // 127.0.0.1/8 is considered localhost for IPv4.
  window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/)
)

// Option 1
router.onReady(() => {
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script',`https://www.google-analytics.com/analytics.js`,'ga')

  ga('create', 'UA-145146446-1','auto')
  
  // Prevent any hits from being sent to Google Analytics
  if (isLocalhost) {
    ga('set', 'sendHitTask', null)
  }

  router.afterEach((to, from) => {
    ga('set', 'page', to.fullPath)
    ga('send', 'pageview')
  })
})


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
