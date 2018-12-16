<template>
  <div class="sidebar-item" @click.prevent="updateArticleList">
    <a href="#" class="btn round-btn sidebar-btn topic-btn">
      <span class="f-15">{{topic.name}}</span>
      <span class="badge f-12">{{topic.total}}</span>
    </a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  props: ['topic'],
  methods: {
    ...mapActions(['fetchArticleListBy']),
    ...mapMutations(['assignQuery']),
    updateArticleList (e) {
      const query = {
        name: 'topic',
        id: this.topic.id
      }
      this.assignQuery(query)
      this.fetchArticleListBy(query)
    }
  }
}
</script>

<style>
.topic-btn .badge {
  background: #30908d;
}
</style>
