/* article list
 * the only one methods to update article list:
 *   - update store.state.query
 */
<template>
  <div v-if="hasArticles" class="article-list">
    <article-item
      :article="article"
      v-for="article in articles"
      :key="article.id"
    ></article-item>
    <!-- pagination -->
    <pagination></pagination>
  </div>
  <div v-else>
    <p>没找到对应的文章</p>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import ArticleItem from './article-item.vue'
import Pagination from '../pagination.vue'

export default {
  components: {
    ArticleItem,
    Pagination
  },
  computed: {
    ...mapState(['artList', 'artQuery']),
    ...mapGetters(['articles']),
    hasArticles () {
      return typeof this.articles !== "undefined" && this.articles.length !== 0
    }
  },
  methods: {
    ...mapActions([
      'fetchArticleListBy'
    ])
  },
  watch: {
    artQuery: {
      handler () {
        this.fetchArticleListBy(this.artQuery)
      }
    }
  }
}
</script>
