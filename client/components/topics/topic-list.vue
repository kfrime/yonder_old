<template>
  <!--<div class="col-md-offset-2 col-md-10">-->
    <!-- 主题列表 -->
    <div class="topic-list">
      <div class="topic-title">文章主题</div>

      <topic-item
        :topic = "topic"
        v-for="topic in topics"
        :key="topic.id"
      ></topic-item>
    </div>
  <!--</div>-->
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import TopicItem from './topic-item.vue'

export default {
  components: {
    TopicItem
  },
  computed: {
    ...mapState(['topicList', 'topicQuery']),
    ...mapGetters(['topics'])
  },
  methods: {
    ...mapActions(['fetchTopicListBy'])
  },
  watch: {
    topicQuery: {
      handler () {
        this.fetchTopicListBy(this.topicQuery)
      }
    }
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

