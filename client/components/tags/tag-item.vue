<template>
  <div class="sidebar-item" @click.prevent="updateArticles">
    <a href="#" class="btn round-btn sidebar-btn tag-btn">
      <span class="f-15">{{tag.name}}</span>
      <span class="badge f-12">{{tag.total}}</span>
    </a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  props: ['tag'],
  methods: {
    ...mapActions(['fetchArticleListBy']),
    ...mapMutations(['assignQuery']),
    updateArticles (e) {
      const query = {
        name: 'tag',
        id: this.tag.id
      }
      this.assignQuery(query)
      this.fetchArticleListBy(query)
    }
  }
}
</script>

<style>

.tag-btn .badge {
  background: #e09c3b;
}
</style>