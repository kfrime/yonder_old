<template>
  <!--文章分类-->
  <div class="card border-0 rounded-0 px-3 mb-2 mb-md-3" id="category-card">
    <div class="card-header bg-white px-0">
      <strong><i class="fa fa-book mr-2 f-17"></i>文章分类</strong>
    </div>

    <ul class="list-group list-group-flush f-16">
      <topic-item :topic="topic" v-for="topic in topics" :key="topic.id"></topic-item>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import TopicItem from './topic-item.vue'

export default {
  components: {
    TopicItem
  },
  computed: {
    ...mapState(['topics'])
  },
  methods: {
    ...mapActions(['fetchAllTopics'])
  },
  mounted () {
    this.fetchAllTopics()
    // console.log('topics after mounted', this.topics)
  }
}
</script>

