// 前端页面路由集合
import AppMain from '../views/app-main.vue'
import ArticleDetail from '../views/article-detail.vue'

export default [
  {
    path: '/',
    redirect: '/app'
  },
  {
    path: '/app',
    component: AppMain
  },
  {
    path: '/article/:id',
    props: true,
    component: ArticleDetail
  }
]
