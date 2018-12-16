<template>
  <div class="sidebar-item">
    <router-link :to="`/topic/${topic.id}`" class="btn round-btn sidebar-btn topic-btn">
      <span class="f-15">{{topic.name}}</span>
      <span class="badge f-12">{{topic.total}}</span>
    </router-link>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  props: ['topic'],
  methods: {
    ...mapActions(['fetchArticleListBy']),
    ...mapMutations(['assignArtQuery']),
  }
}
</script>

<style>
.topic-btn .badge {
  background: #30908d;
}
</style>
