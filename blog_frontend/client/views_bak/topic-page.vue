<template>
  <div class="container app-main">
    <div class="row">
      <!--文章列表-->
      <div class="col-lg-8">
        <div class="description bg-white px-3 pt-3 pb-1">
          <p class="float-right mb-0">共<span class="mx-2 text-info">{{ topic.total }}</span>篇</p>
          <h1 class="f-17"><strong>文章分类：{{ topic.name }}</strong></h1>
          <p class="f-16">{{ topic.desc }}</p>
        </div>
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
  props: ['id'],
  components: {
    ArticleList,
    TopicList,
    TagList
  },
  computed: {
    ...mapState(['topics', 'articles', 'tags', 'topic'])
  },
  mounted () {
    this.fetchOneTopic(this.id)
    this.fetchArticlesByTopic(this.id)
    this.fetchAllTopics()
    this.fetchAllTags()
  },
  methods: {
    ...mapActions([
      'fetchOneTopic',
      'fetchArticlesByTopic',
      'fetchAllTopics',
      'fetchAllTags'
    ])
  }
}
</script>