<template>
  <div>
    <ButtonGroup >
      <Button :size="buttonSize" @click="updateArticle"><Icon type="ios-code" /></Button>
    </ButtonGroup>
  </div>
</template>

<script>
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
      }
    }
  }
</script>
