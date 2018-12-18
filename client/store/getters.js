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
  artPages (state) {
    const resp = state.artResp
    return resp.count / resp.results.length
  }
}
