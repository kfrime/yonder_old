<template>
  <div>
    article detail page: _id.vue
  </div>
</template>

<script>
  import request from '~/api/request'

  export default {
    validate ({ params }) {
      // 必须是number类型
      return /^\d+$/.test(params.id)
    },
    asyncData (ctx) {
      // console.log("article asyncData")
      console.log("params:", ctx.params)
      console.log("query:", ctx.query)

      return Promise.all([
        request.getArticles({
          client: ctx.req,
        })
      ]).then(resp => {
        console.log("get data:", resp)

        return {

        }
      }).catch(err => {
        console.log("catch error:", err)
        ctx.error({ message: "not found", statusCode: 404 })
      })
    },
  }
</script>