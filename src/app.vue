<template>
  <div id="app">
    <Header></Header>
    <div class="test">{{ content }}</div>
  </div>
</template>

<script>
import Header from './blog/header.vue'

export default {
  components: {
    Header
  },
  data () {
    return {
      content: 'Hello Vue'
    }
  }
}
</script>

<style lang="stylus" scoped>
.test{
  color red
  text-align center
}
</style>