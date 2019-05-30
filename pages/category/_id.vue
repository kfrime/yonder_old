<template>
  <div>
    <Card :bordered="false">
      <p slot="title">
        java
        <!--{{cate.Title}}-->
      </p>
    </Card>
    <article-item
      v-for="ar in articles"
      :article="ar"
      :key="ar.ID"
    >
    </article-item>
    <!--<div v-for="ar in articles">{{ar}}</div>-->
  </div>
</template>

<script>
  import request from '~/api/request'
  import ArticleItem from '~/components/ArticleItem'

  export default {
    validate ({ params }) {
      // 必须是number类型
      return /^\d+$/.test(params.id)
    },
    data () {
      return {

      }
    },
    asyncData (ctx) {
      // console.log("article asyncData")
      console.log("params:", ctx.params)
      console.log("query:", ctx.query)

      return Promise.all([
        request.getCates({
          client: ctx.req
        }),
        request.getArticles({
          client: ctx.req,
          query: {
            cateId: ctx.params.id
          }
        })
      ]).then(resp => {
        console.log("get data:", resp)
        // categories
        let cates = resp[0].data.cateList || []
        // console.log("cates", cates)
        ctx.store.commit('setCates', cates)

        // articles
        let articles = resp[1].data.al || []
        // console.log("articles", articles)
        ctx.store.commit('setArticles', articles)

        return {
          articles: articles
        }
      }).catch(err => {
        console.log("catch error:", err)
        ctx.error({ message: "not found", statusCode: 404 })
      })
    },
    layout: "default",
    components: {
      'article-item': ArticleItem
    }
  }
</script>