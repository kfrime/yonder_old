<template>
  <div class="container app-main">
    <div class="row">
      <!--文章列表-->
      <div class="col-lg-8">
        <article-list></article-list>
      </div>
      <div class="col-lg-4">
        <topic-list></topic-list>
      </div>
    </div>        <!-- end: row -->
  </div>          <!-- end: container -->
</template>

<script>
import ArticleList from './article-list.vue'
import TopicList from './topic-list.vue'

export default {
  components: {
    ArticleList,
    TopicList
  }
}
</script>

<style lang="stylus">
</style>
