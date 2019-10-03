import Vue from 'vue'
import Component from './extend'

const NotificationClass = Vue.extend(Component)

const instances = [] // 创建的实例的列表
let seed = 1 // 用作实例的id

const removeInstance = (instance) => {
  if (!instance) return

  const len = instances.length
  const index = instances.findIndex(inst => instance.id === inst.id)

  instances.splice(index, 1)

  if (len <= 1) return
  const removeHeight = instance.vm.height
  for (let i = index; i < len - 1; i++) {
    instances[i].verticalOffset =
      parseInt(instances[i].verticalOffset) - removeHeight - 16
  }
}

const nofify = (options) => {
  const {
    autoClose, ...rest
  } = options

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

  // 计算高度，默认第一个放到右上角，如果有多个，依次向下叠加
  const navbarHeight = document.getElementById('blog-navbar').offsetHeight
  let verticalOffset = navbarHeight   // 如果放到右下角，设为0
  instances.forEach(item => {
    verticalOffset += item.$el.offsetHeight + 16 // 间隔16个像素
  })

  verticalOffset += 16 // 比屏幕边框高16个像素
  instance.verticalOffset = verticalOffset
  instances.push(instance)
  instance.vm.$on('closed', () => {
    // notification关闭后，删除其对应的组件实例，防止占用内存
    removeInstance(instance)
    document.body.removeChild(instance.vm.$el) // 删除DOM里的结点
    instance.vm.$destroy()
  })
  instance.vm.$on('close', () => {
    instance.vm.visible = false
  })
  return instance.vm
}

export default nofify
