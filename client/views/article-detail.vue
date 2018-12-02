<template>
  <div class="container">
    <!--<div class="content">article detail</div>-->
    <div class="content">author: {{ article.author.name }}</div>
    <div class="content">title: {{ article.title }}</div>
    <div class="content">summary: {{ article.summary }}</div>
    <div class="content">content: {{ article.text }}</div>
    <!--<div class="text">getter text: {{ text }}</div>-->
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
export default {
  props: ['id'],
  computed: {
    ...mapState(['article']),
    ...mapGetters(['text'])
  },
  mounted () {
    this.fetchOneArticle(this.id)
  },
  methods: {
    ...mapActions(['fetchOneArticle'])
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
