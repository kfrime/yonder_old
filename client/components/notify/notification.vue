<template>
  <transition name="fade">
    <div class="bg-secondary text-white notification">
      <span class="content">{{content}}</span>
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
  }
}
</script>

<style scoped>
.notification {
  display: inline-flex;
  align-items: center;
  padding: 0.4rem;
  min-width: 280px;
  box-shadow: 0px 3px 5px;
  flex-wrap: wrap;
  transition: all .3s;
}
.content {
  padding: 0
}
</style>
