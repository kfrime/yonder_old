// vuex mutations

export default {
  fillArticles (state, resp) {
    state.artResp = resp
    // console.log('fillArticles', resp)
  },
  fillTopics (state, resp) {
    state.topicResp = resp
  },
  fillTags (state, resp) {
    // console.log('fillTags', resp)
    state.tagResp = resp
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
    state.artQuery = query
  },
  assignTagQuery (state, query) {
    state.tagQuery = query
  }
}
