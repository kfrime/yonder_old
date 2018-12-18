<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <!-- tag 的描述说明 -->
        <div class="card summary">
          <div class="card-body summary-body summary-tag">
            <div class="summary-header f-16 pb-1">
              <span class="float-right mb-0 mr-1">共<span class="text-primary mx-2">{{tag.total}}</span>篇</span>
              <span class="">文章标签：<span class="text-dark"><strong>{{tag.name}}</strong></span></span>
            </div>
            <p class="f-15 mb-1">{{tag.desc}}</p>
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
  import { mapState, mapActions, mapMutations } from 'vuex'
  import ArticleList from '../components/articles/article-list.vue'
  import TopicList from '../components/topics/topic-list.vue'
  import TagList from '../components/tags/tag-list.vue'

  export default {
    props: ['id'],
    components: {
      ArticleList,
      TopicList,
      TagList
    },
    computed: {
      ...mapState(['tag'])
    },
    methods: {
      ...mapActions(['fetchOneTag']),
      ...mapMutations(['assignArtQuery', 'assignTopicQuery', 'assignTagQuery'])
    },
    beforeRouteUpdate (to, from, next) {
      // vue-router 复用同一组件，但是路由不一样时，这个会被触发，如： '/api/tags/:id'
      const id = to.params.id
      this.fetchOneTag(id)
      this.assignArtQuery({
        name: 'tag',
        id: id
      })
      // console.log('beforeRouteUpdate, query:', id)
      next()
    },
    mounted () {
      this.fetchOneTag(this.id)
      this.assignArtQuery({
        name: 'tag',
        id: this.id
      })
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
