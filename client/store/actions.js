import api from '../api/api'

const handleError = (err) => {
  console.log('err', err)
}

export default {
  /*
  fetchAllArticles ({ commit }) {
    api.getAllArticles()
      .then(data => {
        // console.log('fetchAllArticles', data)
        commit('fillArticles', data.results)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticlesByTopic ({ commit }, topicId) {
    api.getArticleByTopic(topicId)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillArticles', data.results)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticlesByTag ({ commit }, tagId) {
    api.getArticleByTag(tagId)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillArticles', data.results)
      })
      .catch(err => {
        handleError(err)
      })
  },
  */
  fetchOneArticle ({ commit }, id) {
    api.getOneArticle(id)
      .then(data => {
        // console.log('assignArticle', data)
        commit('assignArticle', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchAllTopics ({ commit }) {
    api.getAllTopics()
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillTopics', data.results)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchOneTopic ({ commit }, id) {
    api.getTopic(id)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('assignTopic', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchAllTags ({ commit }) {
    api.getAllTags()
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillTags', data.results)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchOneTag ({ commit }, id) {
    api.getTag(id)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('assignTag', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchTagByArticleId ({ commit }, articleId) {
    api.getTagByArticleId(articleId)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillTags', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticleListBy ({ commit }, { filter, id }) {
    // console.log('fetchArticleList, filter:', filter, 'id:', id)
    api.getArticleList(filter, id)
      .then(data => {
        // console.log('fetchArticleList', data)
        commit('fillArticles', data.results)
      })
      .catch(err => {
        handleError(err)
      })
  }
}
