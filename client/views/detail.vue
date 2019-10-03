<template>
  <div class="container article-detail">
    <div class="row">
      <div class="col-lg-9">
        <!-- 显示文章路径 -->
        <div aria-label="breadcrumb" class="article-location">
          <ul class="breadcrumb">
            <li class="breadcrumb-item">
              <router-link :to="{ name: 'home' }" class="location-item">首页</router-link>
            </li>
            <li class="breadcrumb-item">
              <!--:to="`/topics/${article.topic.id}/${article.topic.slug}`"-->
              <!--:to="{ name: 'topic', params: { id: article.topic.id, slug: article.topic.slug }}"-->
              <router-link
                :to="`/topics/${article.topic.id}/${article.topic.slug}`"
                class="location-item"
              >
                {{article.topic.name}}
              </router-link>
            </li>
            <li class="breadcrumb-item active" aria-current="page">{{article.title}}</li>
          </ul>
        </div>

        <!-- 文章详情 -->
        <div class="card detail-card">
          <div class="card-body py-2">
            <div class="text-center detail-title">
              <h1 class="f-17 my-2 text-dark">{{article.title}}</h1>
            </div>
            <div class="text-center py-2 detail-summary">
              <span class="text-secondary">
                <i class="fas fa-user mx-1"></i>{{article.author.name}}<i class="mr-1"></i>
                <i class="far fa-calendar-check mx-1"></i>{{article.ctime}}
              </span>
            </div>
            <!-- 文章内容 -->
            <div class="pt-3 detail-text" v-html="article.text"></div>
          </div>
        </div>

        <div class="article-extend">
          <!-- tag list -->
          <div class="simple-tag-list">
            <i class="fas fa-tags mx-1 text-secondary"></i>
            <simple-tag-item
              :tag = "tag"
              v-for="tag in tags"
              :key="tag.id"
            ></simple-tag-item>
          </div>

          <!-- pre and next article -->
          <div class="neighbor-articles mt-1">
            <div v-if="article.pre" class="float-left">
              <!--:to="`/articles/${article.pre.id}/${article.pre.slug}`"-->
              <router-link
                :to="{ name: 'detail', params: { id: article.pre.id, slug: article.pre.slug }}"
                class="f-16 article-title"
              ><i class="fas fa-angle-double-left mx-1 text-secondary"></i>{{article.pre.title}}
              </router-link>
            </div>

            <div v-if="article.next" class="float-right">
              <!--:to="`/articles/${article.next.id}/${article.next.slug}`"-->
              <router-link
                :to="{ name: 'detail', params: { id: article.next.id, slug: article.next.slug }}"
                class="f-16 article-title d-md-block"
              >{{article.next.title}}<i class="fas fa-angle-double-right mx-1 text-secondary"></i>
              </router-link>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import SimpleTagItem from '../components/tags/simple-tag-item.vue'

export default {
  components: {
    SimpleTagItem
  },
  props: ['id', 'slug'],
  computed: {
    ...mapState(['article']),
    tags () {
      return this.article.tags
    }
  },
  methods: {
    ...mapActions(['fetchOneArticle', 'fetchTagListBy'])
  },
  mounted () {
    this.fetchOneArticle(this.id)
    // console.log('article detail:', this.article)
  },
  beforeRouteUpdate (to, from, next) {
    // vue-router 复用同一组件，但是路由不一样时，这个会被触发
    const id = to.params.id
    this.fetchOneArticle(id)
    next()
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
