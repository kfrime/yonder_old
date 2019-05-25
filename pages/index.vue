<template>
  <div>
    home page
    <div v-for="ar in articles">{{ar}}</div>
  </div>
</template>

<script>
  import request from '~/api/request'

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
  }
</script>