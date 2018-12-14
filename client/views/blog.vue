<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <!-- 文章列表 -->
        <div class="article-list">
          <article-item
            :article="article"
            v-for="article in articles"
            :key="article.id"
          ></article-item>
        </div>
      </div>

      <div class="col-lg-4 sidebar-module">
        <!-- 主题列表 -->
        <div class="col-md-offset-2 col-md-10">
          <div class="blog-card topic-list">
            <div class="topic-title">Topics</div>

            <topic-item
              :topic = "topic"
              v-for="topic in topics"
              :key="topic.id"
            ></topic-item>
          </div>

          <!-- 标签列表 -->
          <div class="blog-card tag-list">
            <div class="tag-title">Tags</div>

            <tag-item
              :tag = "tag"
              v-for="tag in tags"
              :key="tag.id"
            ></tag-item>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ArticleItem from '../components/article-item.vue'
import TopicItem from '../components/topic-item.vue'
import TagItem from '../components/tag-item.vue'

export default {
  components: {
    ArticleItem,
    TopicItem,
    TagItem
  },
  computed: {
    ...mapState(['articles', 'topics', 'tags'])
  },
  mounted () {
    this.fetchAllArticles()
    this.fetchAllTopics()
    this.fetchAllTags()

    console.log('articles', this.articles)
    console.log('topics', this.topics, this.tags)
    console.log('tags', this.tags)
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

<style>
.blog-card {
  border: none;
  /*background: #f4f4f4;*/
}
.topic-list, .tag-list {
  padding: 0.5rem;
}
.topic-title, .tag-title{
  padding-bottom: 0.5rem;
}
</style>
