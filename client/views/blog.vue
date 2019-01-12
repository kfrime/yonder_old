<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <!-- 文章列表 -->
        <notification content="test notify "/>
        <article-list></article-list>
      </div>

      <!-- sidebar -->
      <div class="col-lg-4 sidebar-module">
        <div class="col-md-offset-2 col-md-10">
          <!-- 主题列表 -->
          <topic-list></topic-list>
          <!-- 标签列表 -->
          <tag-list></tag-list>
        </div>
      </div>
      <!-- end sidebar -->
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import ArticleList from '../components/articles/article-list.vue'
import TopicList from '../components/topics/topic-list.vue'
import TagList from '../components/tags/tag-list.vue'
// import SummaryList from '../components/summary/summary-list.vue'

export default {
  components: {
    // SummaryList,
    ArticleList,
    TopicList,
    TagList
  },
  methods: {
    ...mapMutations(['assignArtQuery', 'assignTopicQuery', 'assignTagQuery'])
  },
  mounted () {
    const query = {
      name: 'all',
      id: null
    }
    this.assignArtQuery(query)
    this.assignTopicQuery(query)
    this.assignTagQuery(query)
  }
}
</script>
