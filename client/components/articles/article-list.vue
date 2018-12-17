/* article list
 * the only one methods to update article list:
 *   - update store.state.query
 */
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
    ...mapState(['artResp', 'artQuery']),
    ...mapGetters(['articles'])
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
