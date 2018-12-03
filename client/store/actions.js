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
        // console.log('assignArticle', resp)
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
  },
  fetchOneTopic ({ commit }, id) {
    api.getTopic(id)
      .then(resp => {
        // console.log('fetchAllTopics', resp)
        commit('assignTopic', resp)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchAllTags ({ commit }) {
    api.getAllTags()
      .then(resp => {
        // console.log('fetchAllTopics', resp)
        commit('fillTags', resp)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchOneTag ({ commit }, id) {
    api.getTag(id)
      .then(resp => {
        // console.log('fetchAllTopics', resp)
        commit('assignTag', resp)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticlesByTopic ({ commit }, topicId) {
    api.getArticleByTopic(topicId)
      .then(resp => {
        // console.log('fetchAllTopics', resp)
        commit('fillArticles', resp.results)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticlesByTag ({ commit }, tagId) {
    api.getArticleByTag(tagId)
      .then(resp => {
        // console.log('fetchAllTopics', resp)
        commit('fillArticles', resp.results)
      })
      .catch(err => {
        handleError(err)
      })
  }
}
