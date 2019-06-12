<template>
  <div>
    <ButtonGroup >
      <Button :size="buttonSize" @click="updateArticle"><Icon type="ios-code" /></Button>
      <Button :size="buttonSize" @click="deleteArticle">
        <Icon type="ios-close" />
        <!--<Icon type="ios-trash-outline" />-->
      </Button>
    </ButtonGroup>
  </div>
</template>

<script>
  import request from '~/api/request'

  export default {
    props: ["article"],
    data () {
      return {
        buttonSize: "small",
      }
    },
    methods: {
      updateArticle () {
        this.$router.push("/article/update/" + this.article.ID)
      },
      deleteArticle () {
        console.log('delete article')
        console.log(this.$router.history.current)
        let self = this
        request.deleteArticle({
          params: {
            // id: this.article.ID,
          }
        }).then(resp => {
          if (resp.code === 0) {
            this.$Message.info("delete article success")
            // todo: when current router is '/', not work
            this.$router.push('/')
          } else {
            this.$Message.error({
              duration: 3,
              closable: true,
              content: resp.message || resp.msg,
            })
          }
        }).catch(err => {
          this.$Message.error({
            duration: 3,
            closable: true,
            content: err.message || err.msg,
          })
        })
      }
    }
  }
</script>
