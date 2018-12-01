<template>
  <div id="app">
    <Header></Header>
    <div class="content">{{ author }} {{ content }}</div>
    <div class="blog">{{ blog }}</div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import Header from './views/header.vue'

export default {
  components: {
    Header
  },
  mounted () {
    console.log('vuex store', this.$store)
  },
  computed: {
    ...mapState({
      content: (state) => state.content,
      author: (state) => state.author
    }),
    ...mapGetters({
      blog: 'blog'
    })
  }
}
</script>

<style lang="stylus" scoped>
.content, .blog{
  text-align center
}
.content{
  color #6a1868
}
</style>