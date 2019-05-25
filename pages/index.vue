<template>
  <div>
    home page
  </div>
</template>

<script>
  import request from '~/api/request'

  export default {
    asyncData (ctx) {
      console.log("index asyncData")
      return Promise.all([
        request.getArticles({
          client: ctx.req,
        })
      ]).then(data => {
        console.log("get data:", data)
      }).catch(err => {
        console.log(err.message)
        // ctx.error({ message: "not found", statusCode: 404 })
      })
    },
    data () {
      return {
      }
    },
    layout: 'default',
  }
</script>