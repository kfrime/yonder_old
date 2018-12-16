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
    path: '/topic/:id',
    props: true,
    component: () => import('../views/topic.vue')
  },
  /*
  {
    path: '/tag/:id',
    props: true,
    component: () => import('../views/tag-page.vue')
  }
  */
]
