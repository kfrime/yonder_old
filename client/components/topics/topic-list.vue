<template>
  <!--<div class="col-md-offset-2 col-md-10">-->
    <!-- 主题列表 -->
    <div class="topic-list">
      <div class="topic-title">Topics</div>

      <topic-item
        :topic = "topic"
        v-for="topic in topics"
        :key="topic.id"
        @updateArticleListByTopic="updateArticleListByTopic"
      ></topic-item>
    </div>
  <!--</div>-->
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
    ...mapActions(['fetchAllTopics']),
    updateArticleListByTopic (topicId) {
      console.log('updateArticleListByTopic')
    }
  },
  mounted () {
    this.fetchAllTopics()
  }
}
</script>

<style>
.topic-list{
  padding: 0.5rem;
}
.topic-title{
  padding-bottom: 0.5rem;
}
</style>

