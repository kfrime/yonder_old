// default vuex state

const normalResp = {
  page: {
    count: 0,
    current: 0,
    pre: null,
    next: null,
    pages: 0
  },
  data: []
}

export default {
  // 根据这个来判断文章列表页是否展示topic或者tag的信息
  artQuery: {},
  topicQuery: {},
  tagQuery: {},
  archiveQuery: {},
  query: {
    filter: null,
    id: null,
    page: null
  },

  /* 列表 */
  artList: normalResp,
  topicList: normalResp,
  tagList: normalResp,
  archiveList: {
    count: null,
    data: []
  },

  /* 详情 */
  topic: {},
  tag: {},
  article: {
    author: {},
    topic: {},
    tags: []
  }
}
