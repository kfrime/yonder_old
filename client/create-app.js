import Vue from 'vue'
import App from './app.vue'

// import './assets/styles/bootstrap.min.css'
import './assets/styles/bootstrap.css'
import './assets/styles/normalize.css'
import './assets/styles/blog.css'
import './assets/styles/sidebar.css'

import createStore from './store/store'
import createRouter from './router/router'
import Notification from './components/notify'

Vue.use(Notification)

export default () => {
  const store = createStore()
  const router = createRouter()

  const app = new Vue({
    store,
    router,
    render: (h) => h(App)
  }).$mount('#root')

  return { app, router, store }
}

