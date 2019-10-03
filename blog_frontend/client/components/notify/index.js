import Notification from './notification.vue'
import notify from './notify'

export default (Vue) => {
  Vue.component(Notification.name, Notification)
  // 扩展Vue内置的方法，全局可以通过this.xx来调用这些方法
  Vue.prototype.$notify = notify
}
