<template>
  <div id="app">
    <Header></Header>
    <div class="test">{{ content }}</div>
  </div>
</template>

<script>
import Header from './views/header.vue'

export default {
  components: {
    Header
  },
  mounted () {
    console.log('vuex store', this.$store)
  },
  computed: {
    content () {
      return this.$store.state.content
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