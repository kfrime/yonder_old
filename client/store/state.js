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
  artResp: {},
  topicResp: {},
  tagResp: {},

  topic: {},
  tag: {},
  article: {
    author: {},
    topic: {},
    tags: []
  }
}
