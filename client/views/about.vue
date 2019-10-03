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
              <span>
                <i class="fas fa-user mx-1"></i>{{article.author.name}}<i class="mr-1"></i>
                <i class="far fa-calendar-check mx-1"></i>{{article.utime}}
              </span>
            </div>
              <!--<span class="mx-2">{{article.author.name}}</span>创建于：{{article.ctime}}</div>-->
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
</style>
