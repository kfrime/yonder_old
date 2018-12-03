// 前端页面路由集合
// import AppMain from '../views/app-main.vue'
// import ArticleDetail from '../views/article-detail.vue'

export default [
  {
    path: '/',
    component: () => import('../views/app-main.vue')
  },
  {
    path: '/article/:id',
    props: true,
    component: () => import('../views/article-detail.vue')
  },
  {
    path: '/topic/:id',
    props: true,
    component: () => import('../views/topic-page.vue')
  },
  {
    path: '/tag/:id',
    props: true,
    component: () => import('../views/tag-page.vue')
  }
]
