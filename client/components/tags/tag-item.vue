<template>
  <div class="sidebar-item" @click="updateArticles">
    <a href="#" class="btn round-btn sidebar-btn tag-btn">
      <span class="f-15">{{tag.name}}</span>
      <span class="badge f-12">{{tag.total}}</span>
    </a>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: ['tag'],
  methods: {
    ...mapActions(['fetchArticleListBy']),
    updateArticles (e) {
      this.fetchArticleListBy({
        name: 'tag',
        id: this.tag.id
      })
    }
  }
}
</script>

<style>

.tag-btn .badge {
  background: #e09c3b;
}
</style>