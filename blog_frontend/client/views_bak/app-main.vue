<template>
  <div class="container app-main">
    <div class="row">
      <!--文章列表-->
      <div class="col-lg-8">
        <article-list :articles="articles"></article-list>
      </div>
      <div class="col-lg-4">
        <topic-list :topics="topics"></topic-list>
        <tag-list :tags="tags"></tag-list>
      </div>
    </div>        <!-- end: row -->
  </div>          <!-- end: container -->
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ArticleList from './article-list.vue'
import TopicList from './topic-list.vue'
import TagList from './tag-list.vue'

export default {
  components: {
    ArticleList,
    TopicList,
    TagList
  },
  mounted () {
    this.fetchAllArticles()
    this.fetchAllTopics()
    this.fetchAllTags()
  },
  computed: {
    ...mapState(['articles', 'topics', 'tags'])
  },
  methods: {
    ...mapActions([
      'fetchAllArticles',
      'fetchAllTopics',
      'fetchAllTags'
    ])
  }
}
</script>

<style lang="stylus">
</style>
