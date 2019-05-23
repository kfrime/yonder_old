import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = () => new Vuex.Store({
  state: {
    artilces: []
  },
  mutations: {
    setArticles (state, articles) {
      state.articles = articles
    }
  }
})

export const state = () => {
  artilces: []
}

export const mutations = {
  setArticles (state, articles) {
    state.articles = articles
  }
}

// export default store
