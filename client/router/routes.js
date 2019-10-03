// 前端页面路由集合

export default [
  {
    name: 'home',
    path: '/',
    component: () => import('../views/blog.vue')
  },
  {
    name: 'detail',
    path: '/articles/:id/:slug',
    props: true,
    component: () => import('../views/detail.vue')
  },
  {
    name: 'topic',
    path: '/topics/:id/:slug',
    props: true,
    component: () => import('../views/topic.vue')
  },
  {
    name: 'tag',
    path: '/tags/:id/:slug',
    props: true,
    component: () => import('../views/tag.vue')
  },
  {
    name: 'search',
    path: '/search/:search',
    props: true,
    component: () => import('../views/search.vue')
  },
  {
    name: 'archive',
    path: '/archives/',
    component: () => import('../views/archive.vue')
  },
  {
    name: 'about',
    path: '/about/',
    component: () => import('../views/about.vue')
  }
]
