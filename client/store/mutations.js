// vuex mutations

export default {
  fillArticles (state, articles) {
    state.articles = articles
  },

  assignArticle (state, article) {
    state.article = article
  },

  fillTopics (state, topics) {
    // console.log('fillTopics', topics)
    state.topics = topics
  }
}
