<template>
  <div class="article-cell">
    <!--
    { "ID": 1, "CreatedAt": "2019-05-03T18:46:48+08:00", "UpdatedAt": "2019-05-03T18:46:48+08:00",
    "Title": "lua", "UserId": 1, "Username": "admin", "CateId": 1, "CateName": "lua" }
    -->
    <Card>
      <div class="card-body">
        <div class="title">
          <a>{{article.Title}}</a>
        </div>
        <!--<br/>-->
        <Button :size="buttonSize" type="default">{{article.Username}}</Button>
        <Button :size="buttonSize" type="default">{{article.UpdatedAt}}</Button>
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
        buttonSize: "small"
      }
    }
  }
</script>

<style scoped>
  .article-cell {
    padding: 8px;
  }
  .title {
    padding-bottom: 8px;
    font-size: 20px;
    font-weight: normal;
  }
  .card-body {
    /*padding: 0;*/
  }
</style>