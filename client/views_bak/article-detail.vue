<template>
  <div class="container app-main">
    <div class="row">
      <div class="col-lg-9">
        <div aria-label="breadcrumb">
          <ol class="breadcrumb bg-white border-0 rounded-0 mb-2 py-2 f-15">
            <li class="breadcrumb-item">
              <i class="fa fa-home mr-1"></i><a href="/">首页</a>
            </li>
            <li class="breadcrumb-item" v-if="article">
              <router-link :to="`/topic/${article.topic.id}`">{{article.topic.name}}</router-link>
            </li>
            <li class="breadcrumb-item active d-none d-md-block" aria-current="page">{{ article.title }}</li>
            <li class="breadcrumb-item active d-md-none" aria-current="page">当前位置</li>
          </ol>
        </div>
        <div class="card rounded-0 border-0" id="article">
          <div class="card-body px-2 px-md-3 pb-0">
            <h1 class="card-title text-center font-weight-bold text-info">{{ article.title }}</h1>
            <hr>
            <div class="text-center f-13">
              <span class="mx-2" data-toggle="tooltip" data-placement="bottom">
                最后编辑于：{{ article.ctime }}
              </span>
            </div>
            <div class="article-body mt-4 f-17" style="line-height:1.8" v-html="article.text">
              <!--{{ article.text}}-->
              <p class="font-weight-bold text-info">
                <i class="fa fa-bullhorn mx-1"></i>
                原创文章，转载请注明出处：request.build_absolute_uri
              </p>
            </div>
            <!--tags-->
            <div class="tag-cloud my-4">
              <tag-item
                class="tags f-16"
                :tag="tag"
                v-for="tag in tags"
                :key="tag.id"
                @updateArticleListByTag="updateArticleListByTag"
              ></tag-item>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-3">
        <!--<span v-if="article.toc">文章目录</span>-->
        <div class="article-toc d-none d-lg-block f-16" v-if="article" >
          <div v-html="article.toc"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import TagItem from './tag-item.vue'

export default {
  components: {
    TagItem
  },
  props: ['id'],
  computed: {
    ...mapState(['article', 'tags'])
    // ...mapGetters(['text'])
  },
  mounted () {
    this.fetchOneArticle(this.id)
    this.fetchTagByArticleId(this.id)
  },
  methods: {
    ...mapActions(['fetchOneArticle', 'fetchTagByArticleId', 'fetchArticlesByTag']),
    updateArticleListByTag (tagId) {
      console.log('tag id', tagId)
      this.fetchArticlesByTag(tagId)
    }
  }
}
</script>

<style lang="stylus">
  .content, .text{
    text-align center
  }
  .content{
    color #6a1868
  }
</style>
