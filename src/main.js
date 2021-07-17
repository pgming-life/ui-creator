import Vue from 'vue'
import App from '@/App.vue'
import store from '@/store'
import router from '@/router'
import vuetify from './plugins/vuetify'

// Vue.js devtools
// https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd
Vue.config.devtools = true;

// true > issue a developer message on the console.
Vue.config.productionTip = true;

// run Vue application
const vue = new Vue({
  vuetify,              // create UI
  router,               // SPA route
  store,
  render: h => h(App)   // rendering App component
})

// mount #appID on DOM
vue.$mount('#app')
