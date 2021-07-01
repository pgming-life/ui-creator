import Vue from 'vue'
import App from '@/App.vue'
import store from '@/store'
import router from '@/router'
import vuetify from './plugins/vuetify'

// Vue.js devtools
// https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd
Vue.config.devtools = true;

// true の場合の方が開発者向けのメッセージがコンソールによりたくさん出る
Vue.config.productionTip = true;

// Vueアプリケーションを起動
const vue = new Vue({
  vuetify,              // UIクリエイト
  router,               // SPAルーティング
  store,
  render: h => h(App)   // Appコンポーネントを使用
})

// idがappであるDOMにマウント
vue.$mount('#app')
