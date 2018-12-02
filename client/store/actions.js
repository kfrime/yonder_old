import api from '../api/api'

const handleError = (err) => {
  console.log('err', err)
}

export default {
  fetchArticles ({ commit }) {
    api.getAllArticles()
      .then(resp => {
        console.log('fetchArticles', resp)
        commit('fillArticles', resp.results)
      })
      .catch(err => {
        handleError(err)
      })
  }
}
