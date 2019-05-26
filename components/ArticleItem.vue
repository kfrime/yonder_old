<template>
  <div class="article-cell">
    <!--
    { "ID": 1, "CreatedAt": "2019-05-03T18:46:48+08:00", "UpdatedAt": "2019-05-03T18:46:48+08:00",
    "Title": "lua", "UserId": 1, "Username": "admin", "CateId": 1, "CateName": "lua" }
    -->
    <Card :bordered="false">
      <!--todo: to article detail page-->
      <a slot="title" class="article-title">
        {{article.Title}}
      </a>
      <!--todo: edit article-->
      <ButtonGroup slot="extra" v-if="isAdmin">
        <Button :size="buttonSize"><Icon type="ios-code" /></Button>
      </ButtonGroup>

      <div class="card-body">
        <Button :size="buttonSize" type="text">{{article.Username}}</Button>
        <Button :size="buttonSize" type="text">{{article.UpdatedAt}}</Button>
        <!-- todo: to category page -->
        <Button :size="buttonSize" type="info" shape="circle">{{article.CateName}}</Button>
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