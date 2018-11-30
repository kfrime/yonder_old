import Vue from 'vue'
import App from './app.vue'
import './assets/styles/bootstrap.min.css'
// import './assets/styles/github-colorful.css'
import './assets/styles/base.styl'

// const root = document.createEement('div')
// document.body.appendChild(root)

new Vue({
  render: (h) => h(App)
}).$mount('#root')
