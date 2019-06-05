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

const UserRoleAdmin = 1

import { setTokenCookie } from "../libs/util";

export const state = () => ({
  isAdmin: false,
  cates: [],
  articles: [],
  token: null,
  user: null,
})

export const mutations = {
  setCates (state, cates) {
    state.cates = cates
  },
  setArticles (state, articles) {
    state.articles = articles
  },
  setToken (state, token) {
    state.token = token
    setTokenCookie(token)
  },
  setUser (state, user) {
    state.user = user
    // todo: admin name?
    state.isAdmin = (user.Role === UserRoleAdmin)
  },
}

// export default store
