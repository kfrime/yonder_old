// default vuex state

export default {
  articles: [],
  article: {
    id: 1,
    author: 'Tom',
    title: '堆内存',
    summary: '堆内存详解',
    content: '操作系统堆管理器管理：堆管理器是操作系统的一个模块，堆管理内存分配灵活，按需分配。',
    topic: {
      id: 1,
      name: 'OS'
    },
    tags: 'OS',
    ctime: '2018-12-01 10:30:00'
  }
}
