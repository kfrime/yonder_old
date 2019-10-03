<template>
  <transition name="fade" @after-leave="afterLeave" @after-enter="afterEnter">
    <div
      class="text-dark notification px-2 row"
      :style="style"
      v-show="visible"
      @mouseenter="clearTimer"
      @mouseleave="createTimer"
    >
      <span class="message">{{msg}}</span>
      <a class="ml-auto pl-2 text-warning" @click="handleClose">
        <i class="fas fa-times"></i>
      </a>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Notification',
  props: {
    msg: {
      type: String,
      required: true
    }
  },
  computed: {
    style () {
      return {}
    }
  },
  data () {
    return {
      visible: true
    }
  },
  methods: {
    handleClose (e) {
      e.preventDefault()
      this.$emit('close')
    },
    afterLeave () {
      this.$emit('closed') // notification已经关闭，动画消失
    },
    afterEnter () {},
    createTimer () {},
    clearTimer () {}
  }
}
</script>

<style scoped>
.notification {
  background-color: #e9ecef;
  /*background-color: #f4f4f4;*/
  display: inline-flex;
  align-items: center;
  padding: 0.3rem;
  width: 20rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.275);
  flex-wrap: wrap;
  transition: all .3s;
}
.message {
  padding: 0
}
</style>
