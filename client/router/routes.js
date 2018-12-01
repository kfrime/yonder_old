// 前端页面路由集合
import AppMain from '../views/app-main.vue'
import ArticleDetail from '../views/article-detail.vue'

export default [
  {
    path: '/app',
    component: AppMain
  },
  {
    path: '/article',
    component: ArticleDetail
  }
]
