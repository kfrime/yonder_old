<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8">
        <!-- 文章列表 -->
        <div class="article-list">
          <article-item
            :article="article"
            v-for="article in articles"
            :key="article.id"
          ></article-item>
        </div>
      </div>

      <div class="col-lg-4">
        <!-- 主题列表 -->
        <div class="topic-list">
          topics
        </div>

        <!-- 标签列表 -->
        <div class="tag">
          tags
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ArticleItem from '../components/article-item.vue'

export default {
  components: {
    ArticleItem
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