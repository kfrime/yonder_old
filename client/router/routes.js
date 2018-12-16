// 前端页面路由集合

export default [
  {
    path: '/',
    component: () => import('../views/blog.vue')
  },
  {
    path: '/articles/:id',
    props: true,
    component: () => import('../views/detail.vue')
  },
  {
    path: '/topics/:id',
    props: true,
    component: () => import('../views/topic.vue')
  },
  {
    path: '/tags/:id',
    props: true,
    component: () => import('../views/tag.vue')
  }
]
