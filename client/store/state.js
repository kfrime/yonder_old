// default vuex state

export default {
  // 根据这个来判断文章列表页是否展示topic或者tag的信息
  query: {
    name: '',
    id: null
  },
  artResp: {
    count: 0,         // results count
    next: null,       // next page url
    previous: null,   // previous page url
    results: [],      // article results
  },
  topicResp: {
    count: 0,
    next: null,
    previous: null,
    results: [],
  },
  tagResp: {
    count: 0,
    next: null,
    previous: null,
    results: [],
  },
  topic: {
    id: null,
    name: '',
    slug: '',
    desc: '',
    total: 0
  },
  tag: {
    id: null,
    name: '',
    slug: '',
    desc: '',
    total: 0
  }
}
