<template>
  <div class="article-list">
    <!--<article-item :article="article"></article-item>-->
    <article-item :article="article" v-for="article in articles" :key="article.id"></article-item>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import ArticleItem from './article-item.vue'

export default {
  components: {
    ArticleItem
  },
  mounted () {
    this.fetchAllArticles()
  },
  computed: {
    ...mapState({
      articles: (state) => state.articles
    }),
    ...mapGetters({
      text: 'text'
    })
  },
  methods: {
    ...mapActions(['fetchAllArticles'])
  }
}
</script>
