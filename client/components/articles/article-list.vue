<template>
  <div class="article-list">
    <article-item
      :article="article"
      v-for="article in articles"
      :key="article.id"
    ></article-item>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ArticleItem from './article-item.vue'

export default {
  components: {
    ArticleItem
  },
  computed: {
    ...mapState(['articles'])
  },
  methods: {
    ...mapActions([
      'fetchArticleListBy'
    ])
  },
  mounted () {
    this.fetchArticleListBy({
      filter: 'all'
    })
    console.log('articles', this.articles)
  }
}
</script>
