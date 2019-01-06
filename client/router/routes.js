// 前端页面路由集合

export default [
  {
    path: '/',
    component: () => import('../views/blog.vue')
  },
  {
    path: '/articles/:id/:slug',
    props: true,
    component: () => import('../views/detail.vue')
  },
  {
    path: '/topics/:id/:slug',
    props: true,
    component: () => import('../views/topic.vue')
  },
  {
    path: '/tags/:id/:slug',
    props: true,
    component: () => import('../views/tag.vue')
  },
  {
    name: 'search-articles',
    path: '/articles/search/:search',
    props: true,
    component: () => import('../views/search.vue')
  },
  {
    name: 'archive-page',
    path: '/archives/',
    component: () => import('../views/archive.vue')
  },
  {
    name: 'about-blog',
    path: '/about/',
    component: () => import('../views/about.vue')
  }
]
