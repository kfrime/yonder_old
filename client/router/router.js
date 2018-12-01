import Vue from 'vue'
import Router from 'vue-router'

import routes from './routes'

Vue.use(Router)

// 如果只生成一个Router对象然后返回，服务端渲染时会导致内存溢出
// 因为每次生成一个app，共享一个router，app执行完成后以为其用到的router没释放，
// app的内存也不会释放，内存越用越少，最后溢出
// 所以这里每次都生成一个新的Router返回
export default () => {
  return new Router({
    routes
  })
}
