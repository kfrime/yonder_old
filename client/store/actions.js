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
        commit('fillArticles', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticlesByTopic ({ commit }, topicId) {
    api.getArticleByTopic(topicId)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillArticles', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchAllTopics ({ commit }) {
    api.getAllTopics()
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillTopics', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticlesByTag ({ commit }, tagId) {
    api.getArticleByTag(tagId)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillArticles', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchAllTags ({ commit }) {
    api.getAllTags()
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillTags', data)
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
  fetchArticleListBy ({ commit }, query) {
    /* query:
     *   name: 根据什么来获取文章列表: all, topic, tag
     *   id:   topic.id / tag.id
     */
    // console.log('fetchArticleList, query:', query)
    api.getArticleList(query.name, query.id, query.search, query.page)
      .then(data => {
        // console.log('fetchArticleListBy', filter, data)
        commit('fillArticles', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchTopicListBy ({ commit }, query) {
    /* query:
     *   name: 根据什么来获取标签列表: all
     */
    // console.log('fetchTagListBy, query:', query)
    api.getTopicList(query.name, query.id)
      .then(data => {
        commit('fillTopics', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchTagListBy ({ commit }, query) {
    /* query:
     *   name: 根据什么来获取标签列表: all, article
     *   id:   article.id
     */
    // console.log('fetchTagListBy, query:', query)
    api.getTagList(query.name, query.id)
      .then(data => {
        commit('fillTags', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
  fetchArticlesBySearch ({ commit }, query) {
    api.searchArticles(query.value, query.page)
      .then(data => {
        // console.log('fetchAllTopics', data)
        commit('fillArticles', data)
      })
      .catch(err => {
        handleError(err)
      })
  },
}
