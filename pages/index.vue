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
        request.getArticles({
          client: ctx.req,
        })
      ]).then(resp => {
        console.log("get data:", resp)
        let articles = resp[0].data.al || []
        console.log("articles", articles)

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