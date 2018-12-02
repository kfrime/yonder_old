import Vue from 'vue'
import App from './app.vue'

import './assets/styles/bootstrap.min.css'
// import './assets/styles/github-colorful.css'
// import './assets/styles/index.styl'
import './assets/styles/base.css'
import './assets/styles/detail.css'

import createStore from './store/store'
import createRouter from './router/router'

const store = createStore()
const router = createRouter()

// const root = document.createEement('div')
// document.body.appendChild(root)

new Vue({
  store,
  router,
  render: (h) => h(App)
}).$mount('#root')
