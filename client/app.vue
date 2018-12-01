<template>
  <div id="app">
    <Header></Header>
    <div class="content">author: {{ article.author }}</div>
    <div class="content">title: {{ article.title }}</div>
    <div class="content">summary: {{ article.summary }}</div>
    <div class="content">content: {{ article.content }}</div>
    <div class="text">getter text: {{ text }}</div>
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
      article: (state) => state.article
    }),
    ...mapGetters({
      text: 'text'
    })
  }
}
</script>

<style lang="stylus" scoped>
.content, .text{
  text-align center
}
.content{
  color #6a1868
}
</style>