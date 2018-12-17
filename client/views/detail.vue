<template>
  <div class="container article-detail">
    <div class="row">
      <div class="col-lg-9">
        <!-- 显示文章路径 -->
        <div aria-label="breadcrumb" class="article-location">
          <div class="breadcrumb">
            <li class="breadcrumb-item">
              <router-link to="/" class="location-item">首页</router-link>
            </li>
            <li class="breadcrumb-item">
              <router-link :to="`/topics/${article.topic.id}`" class="location-item">
                {{article.topic.name}}
              </router-link>
            </li>
            <li class="breadcrumb-item active" aria-current="page">{{article.title}}</li>
          </div>
        </div>
        <!-- 文章详情 -->
        <div class="card detail-card">
          <div class="card-body py-2">
            <div class="text-center detail-title">
              <h1 class="f-17 my-2 text-dark">{{article.title}}</h1>
            </div>
            <div class="text-center py-2 detail-summary">
              <span class="mx-2">{{article.author.name}}</span>创建于：{{article.ctime}}</div>
            <div class="pt-3 detail-text" v-html="article.text"></div>
            <div class="tag-list">

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  props: ['id'],
  computed: {
    ...mapState(['article']),
  },
  methods: {
    ...mapActions(['fetchOneArticle'])
  },
  mounted () {
    console.log('article detail:', this.article)
    this.fetchOneArticle(this.id)
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
</style>
