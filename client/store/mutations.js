// vuex mutations

export default {
  fillArticles (state, articles) {
    state.articles = articles
  },
  assignArticle (state, article) {
    // 只获取一篇文章
    state.article = article
  },
  fillTopics (state, topics) {
    state.topics = topics
  },
  fillTags (state, tags) {
    // console.log('fillTags', tags)
    state.tags = tags
  }
}
