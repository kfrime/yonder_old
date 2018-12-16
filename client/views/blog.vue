<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <!-- topic 和 tag 的描述说明 -->
        <summary-list></summary-list>
        <!-- 文章列表 -->
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
// import { mapState, mapActions } from 'vuex'
import ArticleList from '../components/articles/article-list.vue'
import TopicList from '../components/topics/topic-list.vue'
import TagList from '../components/tags/tag-list.vue'
import SummaryList from '../components/summary/summary-list.vue'

export default {
  components: {
    SummaryList,
    ArticleList,
    TopicList,
    TagList
  }
}
</script>
