<template>
  <div>
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
    asyncData (ctx) {
      // console.log("index asyncData")
      return Promise.all([
        request.getCates({
          client: ctx.req
        }),
        request.getArticles({
          client: ctx.req,
        })
      ]).then(resp => {
        console.log("get data:", resp)

        let cates = resp[0].data.cateList || []
        console.log("cates", cates)
        ctx.store.commit('setCates', cates)

        // articles
        let articles = resp[1].data.al || []
        console.log("articles", articles)
        ctx.store.commit('setArticles', articles)

        return {
          articles: articles
        }
      }).catch(err => {
        console.log("catch error:", err)
        ctx.error({ message: "not found", statusCode: 404 })
      })
    },
    data () {
      return {
      }
    },
    layout: 'default',
    components: {
      'article-item': ArticleItem
    }
  }
</script>