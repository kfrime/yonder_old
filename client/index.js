import Vue from 'vue'
import App from './app.vue'
// import Vuex from 'vuex'

import './assets/styles/bootstrap.min.css'
// import './assets/styles/github-colorful.css'
import './assets/styles/base.styl'
import createStore from './store/store'

// Vue.use(Vuex)
const store = createStore()

// const root = document.createEement('div')
// document.body.appendChild(root)

new Vue({
  store,
  render: (h) => h(App)
}).$mount('#root')
