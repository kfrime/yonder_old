<template>
  <div>
    <div>
      <Card dis-hover>
        <Breadcrumb>
          <BreadcrumbItem to="/">Home</BreadcrumbItem>
          <BreadcrumbItem :to="`/category/${article.Category.ID}`">{{article.Category.Name}}</BreadcrumbItem>
          <BreadcrumbItem>{{article.Title}}</BreadcrumbItem>
        </Breadcrumb>
      </Card>
    </div>
    <Card dis-hover>
      <div slot="title">
        <h1 class="article-title">{{article.Title}}</h1>
        <div class="article-info">
          <span>{{article.User.Name}}</span>
          <span>{{article.CreatedAt}}</span>
        </div>
      </div>
      <ButtonGroup slot="extra" v-if="isAdmin">
        <Button :size="buttonSize" @click="updateArticle"><Icon type="ios-code" /></Button>
      </ButtonGroup>

      <div>
        {{article.Content}}
      </div>

      <!-- todo: <div>pre article and next article</div>-->
    </Card>
    <!--todo: 添加文章目录 -->
  </div>
</template>

<script>
  import request from '~/api/request'

  export default {
    data () {
      return {
        buttonSize: "small",
        isAdmin: this.$store.state.isAdmin,
      }
    },
    validate ({ params }) {
      // 必须是number类型
      return /^\d+$/.test(params.id)
    },
    asyncData (ctx) {
      // console.log("article asyncData")
      console.log("params:", ctx.params)
      console.log("query:", ctx.query)

      return Promise.all([
        request.getArticleDetail({
          client: ctx.req,
          params: {
            id: ctx.params.id
          }
        })
      ]).then(resp => {
        console.log("get data:", resp)
        let article = resp[0].data.ad || {}

        return {
          article: article
        }
      }).catch(err => {
        console.log("catch error:", err)
        ctx.error({ message: "not found", statusCode: 404 })
      })
    },
    methods: {
      updateArticle () {
        this.$router.push("/article/update/" + this.article.ID)
      }
    },
    layout: "nosidebar",
  }
</script>

<style scoped>
  .article-title {
    /*font-size: 30px;*/
    /*font-weight: 700;*/
    margin-bottom: 10px;
    /*text-align: center;*/
  }
  .article-info {
    /*margin: 5px 8px;*/
  }
</style>