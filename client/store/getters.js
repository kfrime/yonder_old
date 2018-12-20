// vuex getters

export default {
  articles (state) {
    return state.artResp.results
  },
  topics (state) {
    return state.topicResp.results
  },
  tags (state) {
    return state.tagResp.results
  },
  page (state) {
    const page = state.artResp.page
    if (page === undefined) {
      return {
        pages: 0,
        pre: null,
        next: null
      }
    }
    return page
  }
}
