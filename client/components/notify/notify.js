import Vue from 'vue'
import Notification from './extend'

const NotificationClass = Vue.extend(Notification)

const instances = []
let seed = 1

const notify = (options) => {
  const {
    autoClose, ...rest
  } = options

  // 创建一个实例对象
  const instance = new NotificationClass({
    propsData: {
      ...rest
    },
    data: {
      autoClose: autoClose === undefined ? 3000 : autoClose
    }
  })

  const id = `notification_${seed++}`
  instance.id = id
  instance.vm = instance.$mount()   // 生成一个$el对象，还没有插入到DOM里
  document.body.appendChild(instance.vm.$el)    // 插入到全局的DOM里
  instance.vm.visible = true

  // 计算高度
  let verticalOffset = 0 // 默认第一个放到右下角，如果有多个，依次向上叠加
  instances.forEach(item => {
    verticalOffset += item.$el.offsetHeight + 16 // 间隔16个像素
  })

  verticalOffset += 16 // 比屏幕边框高16个像素
  instance.verticalOffset = verticalOffset
  instances.push(instance)

  return instance.vm
}

export default notify
