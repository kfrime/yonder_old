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
import { mapState, mapGetters, mapActions } from 'vuex'
import ArticleItem from './article-item.vue'

export default {
  components: {
    ArticleItem
  },
  computed: {
    ...mapState(['artResp']),
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions([
      'fetchArticleListBy'
    ])
  },
  mounted () {
    const query = {
      name: 'all',
      id: null
    }
    this.fetchArticleListBy(query)
    // console.log('article-list', this.articles)
  }
}
</script>
