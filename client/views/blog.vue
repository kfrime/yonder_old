<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <summary-list></summary-list>
        <!-- 文章列表 -->
        <article-list></article-list>
        <!--<div class="articles-list">-->
          <!--<articles-item-->
            <!--:articles="articles"-->
            <!--v-for="articles in articles"-->
            <!--:key="articles.id"-->
          <!--&gt;</articles-item>-->
        <!--</div>-->
      </div>

      <div class="col-lg-4 sidebar-module">
        <div class="col-md-offset-2 col-md-10">
          <!-- 主题列表 -->
          <topic-list></topic-list>
          <!-- 标签列表 -->
          <tag-list></tag-list>
        </div>
          <!-- 主题列表 -->
          <!--<div class="blog-card topic-list">-->
            <!--<div class="topic-title">Topics</div>-->

            <!--<topic-item-->
              <!--:topic = "topic"-->
              <!--v-for="topic in topics"-->
              <!--:key="topic.id"-->
              <!--@updateArticleListByTopic="updateArticleListByTopic"-->
            <!--&gt;</topic-item>-->
          <!--</div>-->

          <!-- 标签列表 -->
          <!--<div class="blog-card tag-list">-->
            <!--<div class="tag-title">Tags</div>-->

            <!--<tag-item-->
              <!--:tag = "tag"-->
              <!--v-for="tag in tags"-->
              <!--:key="tag.id"-->
              <!--@updateArticleListByTag="updateArticleListByTag"-->
            <!--&gt;</tag-item>-->
          <!--</div>-->
      </div>
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
