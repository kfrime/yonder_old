<template>
  <div class="article-cell">
    <Card :bordered="false">
      <a slot="title" class="article-title"  @click.prevent="toDetailPage">
        {{article.Title}}
      </a>
      <!--todo: edit article-->
      <ButtonGroup slot="extra" v-if="isAdmin">
        <Button :size="buttonSize"><Icon type="ios-code" /></Button>
      </ButtonGroup>

      <div class="card-body">
        <Button :size="buttonSize" type="text">{{article.Username}}</Button>
        <Button :size="buttonSize" type="text">{{article.CreatedAt}}</Button>
        <!-- todo: to category page -->
        <Button :size="buttonSize" type="info" shape="circle" @click="toCatePage">
          {{article.CateName}}
        </Button>
      </div>
    </Card>
  </div>
</template>

<script>
  export default {
    props: ['article'],
    data () {
      return {
        buttonSize: "small",
        isAdmin: this.$store.state.isAdmin || false,
      }
    },
    methods: {
      toDetailPage () {
        this.$router.push("/article/" + this.article.ID)
      },
      toCatePage () {
        this.$router.push("/category/" + this.article.CateId)
      }
    }
  }
</script>

<style scoped>
  .article-cell {
    padding: 8px;
  }
  .article-title {
    font-size: 20px;
  }
</style>