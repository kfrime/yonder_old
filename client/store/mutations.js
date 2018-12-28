// vuex mutations

export default {
  fillArticles (state, resp) {
    state.artList = resp
    // console.log('fillArticles', resp)
  },
  fillTopics (state, resp) {
    state.topicList = resp
  },
  fillTags (state, resp) {
    // console.log('fillTags', resp)
    state.tagList = resp
  },
  fillArchives (state, resp) {
    state.archiveList = resp
  },
  assignArticle (state, article) {
    // 只获取一篇文章
    state.article = article
  },
  assignTopic (state, topic) {
    state.topic = topic
  },
  assignTag (state, tag) {
    state.tag = tag
  },
  assignArtQuery (state, query) {
    // console.log('art query:', query)
    state.artQuery = query
  },
  assignTopicQuery (state, query) {
    state.topicQuery = query
  },
  assignTagQuery (state, query) {
    state.tagQuery = query
  },
  assignArchiveQuery (state, query) {
    state.archiveQuery = query
  }
}
