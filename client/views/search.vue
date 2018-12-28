<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <!-- search 的描述说明 -->
        <div v-if="searched" class="card summary">
          <div class="card-body summary-body summary-topic">
            <div class="summary-header f-16 pb-1">
              <p class="mb-1">搜索：<span class="text-dark mx-1"><strong>{{search}}</strong></span></p>
              <p class="mb-0 mt-1">找到<span class="text-primary mx-2">{{artList.page.count}}</span>篇</p>
            </div>
          </div>
        </div>
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
import { mapState, mapMutations } from 'vuex'
import ArticleList from '../components/articles/article-list.vue'
import TopicList from '../components/topics/topic-list.vue'
import TagList from '../components/tags/tag-list.vue'

export default {
  props: ['search'],
  components: {
    ArticleList,
    TopicList,
    TagList
  },
  computed: {
    ...mapState(['artQuery', 'artList']),
    searched () {
      return typeof this.search !== "undefined" && this.search !== '';
    }
  },
  methods: {
    ...mapMutations(['assignArtQuery', 'assignTopicQuery', 'assignTagQuery'])
  },
  mounted () {
    const query = {
      name: 'all',
      search: this.search
    }
    this.assignArtQuery(query)
    // this.assignTopicQuery(query)
    // this.assignTagQuery(query)
  },
  beforeRouteUpdate (to, from, next) {
    const search = to.params.search
    // console.log('params', to.params)
    this.assignArtQuery({
      name: 'all',
      search: search
    })
    next()
  },
}
</script>
