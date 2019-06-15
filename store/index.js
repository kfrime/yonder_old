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
  // todo: isAdmin set to false
  isAdmin: true,
  cates: [],
  articles: [],
  total: 0,
  cate: null,
  token: null,
  user: null,
  q: '',
})

export const mutations = {
  setCates (state, cates) {
    state.cates = cates
  },
  setCate (state, cate) {
    state.cate = cate
  },
  setArticles (state, articles) {
    state.articles = articles
  },
  setTotal (state, total) {
    state.total = total
  },
  setToken (state, token) {
    state.token = token
    setTokenCookie(token)
  },
  setUser (state, user) {
    state.user = user
    // todo: admin name?
    // state.isAdmin = (user.Role === UserRoleAdmin)
  },
  setSearch (state, q) {
    state.q = q
  }
}

// export default store
