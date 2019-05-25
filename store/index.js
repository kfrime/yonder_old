import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// const store = () => new Vuex.Store({
//   state: {
//     cates: [],
//     articles: []
//   },
//   mutations: {
//     setCates (state, cates) {
//       state.cates = cates
//     },
//     setArticles (state, articles) {
//       state.articles = articles
//     }
//   }
// })

export const state = () => ({
  cates: [],
  articles: []
})

export const mutations = {
  setCates (state, cates) {
    state.cates = cates
  },
  setArticles (state, articles) {
    state.articles = articles
  }
}

// export default store
