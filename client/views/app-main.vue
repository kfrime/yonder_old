<template>
  <div class="container">
    <div class="row">
      <!--文章列表-->
      <div class="col-lg-8">
        <div class="article-list">
          <!--<article-item :article="article"></article-item>-->
          <!-- 后面不要用 idx 作为 key -->
          <article-item :article="article" v-for="article, idx in articles" :key="idx"></article-item>
        </div>
        <!-- 分页 -->
        <!--<article-pagination :page="page"></article-pagination>-->

      </div>

      <!--&lt;!&ndash;右侧边栏&ndash;&gt;-->
      <!--<div class="col-lg-4">-->
      <!--&lt;!&ndash;个人信息&ndash;&gt;-->
      <!--&lt;!&ndash;<div class="home-card"></div>&ndash;&gt;-->

      <!--&lt;!&ndash;文章分类&ndash;&gt;-->
      <!--<div class="card border-0 rounded-0 px-3 mb-2 mb-md-3" id="category-card">-->
      <!--<div class="card-header bg-white px-0">-->
      <!--<strong><i class="fa fa-book mr-2 f-17"></i>文章分类</strong>-->
      <!--</div>-->

      <!--<ul class="list-group list-group-flush f-16">-->
      <!--<topic-item :topic="topic" v-for="topic in topics" :key="topic.id"></topic-item>-->
      <!--</ul>-->
      <!--</div>    &lt;!&ndash; end: category-card &ndash;&gt;-->

      <!--&lt;!&ndash;标签分类&ndash;&gt;-->
      <!--<div class="card border-0 rounded-0 px-3 mb-2 mb-md-3" id="tag-card">-->
      <!--<div class="card-header bg-white px-0">-->
      <!--<strong><i class="fa fa-tags mr-2 f-17"></i>标签列表</strong>-->
      <!--</div>-->

      <!--<div class="card-body px-0 py-3">-->
      <!--<tag-item :tag="tag" v-for="tag in tags" :key="tag.id"></tag-item>-->
      <!--</div>-->
      <!--</div>    &lt;!&ndash; end: tag-card &ndash;&gt;-->
      <!--</div>      &lt;!&ndash; end: right-part &ndash;&gt;-->
    </div>        <!-- end: row -->
  </div>          <!-- end: container -->

  <!--<div class="container">-->
  <!--<article-item :article="article"></article-item>-->
  <!--</div>-->
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import ArticleItem from './article-item.vue'

export default {
  components: {
    ArticleItem
  },
  mounted () {
    this.fetchArticles()
    // console.log('main articles:', articles)
  },
  computed: {
    ...mapState({
      articles: (state) => state.articles
    }),
    ...mapGetters({
      text: 'text'
    })
  },
  methods: {
    ...mapActions(['fetchArticles'])
  }
  // props: ['articles']
}
</script>
