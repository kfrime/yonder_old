<template>
  <div>
    <Card :bordered="false">
      <p slot="title">search:</p>
      <p>{{q}}</p>
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
    data () {
      return {}
    },
    asyncData (ctx) {
      // console.log("article asyncData")
      // console.log("params:", ctx.params)
      // console.log("query:", ctx.query)
      let searchValue = ctx.params.q
      // 优化：分类列表可以不用每次都获取

      return Promise.all([
        request.getCates({
          client: ctx.req
        }),
        request.searchArticle({
          client: ctx.req,
          query: {
            q: searchValue
          }
        })
      ]).then(resp => {
        console.log("get data:", resp)
        // categories
        let cates = resp[0].data.cateList || []
        ctx.store.commit('setCates', cates)

        // articles
        let articles = resp[1].data.al || []
        ctx.store.commit('setArticles', articles)

        return {
          q: searchValue,
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
