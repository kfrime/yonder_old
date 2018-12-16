<template>
  <div class="sidebar-item" @click="updateArticleList">
    <a href="#" class="btn round-btn sidebar-btn topic-btn">
      <span class="f-15">{{topic.name}}</span>
      <span class="badge f-12">{{topic.total}}</span>
      <!--<span class="badge f-12">12345</span>-->
    </a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  props: ['topic'],
  methods: {
    ...mapActions(['fetchArticleListBy']),
    ...mapMutations(['assignFilter']),
    updateArticleList (e) {
      this.assignFilter('topic')
      this.fetchArticleListBy({
        name: 'topic',
        id: this.topic.id
      })
    }
  }
}
</script>

<style>
.topic-btn .badge {
  background: #30908d;
}
</style>
