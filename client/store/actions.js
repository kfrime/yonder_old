import api from '../api/api'

const handleError = (err) => {
  console.log('err', err)
}

export default {
  fetchAllArticles ({ commit }) {
    api.getAllArticles()
      .then(resp => {
        // console.log('fetchAllArticles', resp)
        commit('fillArticles', resp.results)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchOneArticle ({ commit }, id) {
    api.getArticle(id)
      .then(resp => {
        console.log('assignArticle', resp)
        commit('assignArticle', resp)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchAllTopics ({ commit }) {
    api.getAllTopics()
      .then(resp => {
        // console.log('fetchAllTopics', resp)
        commit('fillTopics', resp)
      })
      .catch(err => {
        handleError(err)
      })
  }
}
