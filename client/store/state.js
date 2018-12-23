// default vuex state

export default {
  // 根据这个来判断文章列表页是否展示topic或者tag的信息
  artQuery: {},
  topicQuery: {},
  tagQuery: {},
  /*
  resp: {
    count: 0,         // results count
    next: null,       // next page url
    previous: null,   // previous page url
    results: [],      // article results
  },
  */
  /* 列表 */
  artResp: {
    page: {
      count: 0,
      current: 0,
      pre: null,
      next: null,
      pages: 0
    }
  },
  topicResp: {},
  tagResp: {},

  /* 详情 */
  topic: {},
  tag: {},
  article: {
    author: {},
    topic: {},
    tags: []
  }
}
