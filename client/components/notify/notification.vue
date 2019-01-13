<template>
  <transition name="fade" @after-leave="afterLeave" @after-enter="afterEnter">
    <div
      class="text-dark notification px-2 row"
      :style="style"
      v-show="visible"
    >
      <span class="content">{{content}}</span>
      <a class="ml-auto pl-2 text-warning" @click="handleClose">关闭</a>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Notification',
  props: {
    content: {
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
    handleClose () {
      this.$emit('close')
    },
    afterLeave () {
      this.$emit('closed') // notification已经关闭，动画消失
    },
  }
}
</script>

<style scoped>
.notification {
  background-color: #e9ecef;
  display: inline-flex;
  align-items: center;
  padding: 0.3rem;
  width: 20rem;
  flex-wrap: wrap;
  transition: all .3s;
}
.content {
  padding: 0
}
</style>
