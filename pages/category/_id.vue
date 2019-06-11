<template>
  <div>
    <Card :bordered="false">
      <p slot="title">
        category
      </p>
      <p>{{cate.Name}}</p>
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
  import ArticleItem from '~/components/article/Item'

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
      let cateId = ctx.params.id
      // 优化：分类列表可以不用每次都获取

      return Promise.all([
        request.getCates({
          client: ctx.req
        }),
        request.getArticles({
          client: ctx.req,
          query: {
            cateId: cateId
          }
        })
      ]).then(resp => {
        console.log("get data:", resp)
        // categories
        let cates = resp[0].data.cateList || []
        ctx.store.commit('setCates', cates)

        // 取出当前所属分类的详细信息
        let cate = {}
        for (let c of cates) {
          if (c.ID.toString() === cateId) {
            cate = c
            break
          }
        }

        // articles
        let articles = resp[1].data.al || []
        ctx.store.commit('setArticles', articles)

        return {
          cate: cate,
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