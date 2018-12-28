// vuex getters

export default {
  articles (state) {
    return state.artList.data
  },
  topics (state) {
    return state.topicList.data
  },
  tags (state) {
    return state.tagList.data
  }
}
