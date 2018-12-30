<template>
  <div class="container article-detail">
    <div class="row">
      <div class="col-lg-8 main-module">
        <!-- 文章详情 -->
        <div class="card detail-card">
          <div class="card-body py-2">
            <div class="text-center detail-title">
              <h1 class="f-17 my-2 text-dark">{{article.title}}</h1>
            </div>
            <div class="text-center py-2 detail-summary">
              <span class="mx-2">{{article.author.name}}</span>创建于：{{article.ctime}}</div>
            <!-- 文章内容 -->
            <div class="pt-3 detail-text" v-html="article.text"></div>
          </div>
        </div>
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
import { mapState, mapGetters, mapActions, mapMutations } from 'vuex'

import TopicList from '../components/topics/topic-list.vue'
import TagList from '../components/tags/tag-list.vue'

export default {
  components: {
    TopicList,
    TagList
  },
  computed: {
    ...mapState(['article']),
  },
  methods: {
    ...mapActions(['fetchBlogAbout']),
    ...mapMutations(['assignTopicQuery', 'assignTagQuery'])
  },
  mounted () {
    // console.log('article detail:', this.article)
    this.fetchBlogAbout()
    this.assignTopicQuery({
      name: 'all',
      id: null
    })
    this.assignTagQuery({
      name: 'all',
      id: null
    })
  }
}
</script>

<style>
.article-location {
  background: #f4f4f4;
}
.location-item {
  color: #00a1d6;
}
.detail-card {
  background: #f4f4f4;
  border: none;
}
.detail-title {
  /*border-bottom: 2px solid #e9ecef;*/
}
.detail-summary {
  border-bottom: 2px solid #e9ecef;
}
.detail-text {

}

.article-extend {
  background-color: #f8f9fa;
  padding-top: 0.5rem;
  margin-bottom: 1rem;
}
.simple-tag-list {
  padding: 0.25rem 0.5rem;
}

/* fix float-right not work well */
.neighbor-articles:before,
.neighbor-articles:after {
  content: "";
  display: table;
}
.neighbor-articles:after {
  clear: both;
}
.neighbor-articles {
  display: -ms-flexbox;
  /*display: flex;*/
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  /*padding: 0.75rem 0;*/
  padding: 0.5rem 0.5rem;
  /*margin-bottom: 1rem;*/
  list-style: none;
  background-color: #e9ecef;
  border-radius: 0.25rem;
}
.article-title {
  color: #00a1d6;
}
</style>
