<template>
  <div class="article-cell">
    <!--
    { "ID": 1, "CreatedAt": "2019-05-03T18:46:48+08:00", "UpdatedAt": "2019-05-03T18:46:48+08:00",
    "Title": "lua", "UserId": 1, "Username": "admin", "CateId": 1, "CateName": "lua" }
    -->
    <Card>
      <p slot="title">{{article.Title}}</p>
      <div class="card-body">
        <Button type="text">{{article.Username}}</Button>
        <Button type="text">{{article.UpdatedAt}}</Button>
        <Button type="text">{{article.CateName}}</Button>
      </div>
    </Card>
  </div>
</template>

<script>
  export default {
    props: ['article'],
  }
</script>

<style scoped>
  .article-cell {
    padding: 8px;
  }
  .card-body {
    padding: 0;
  }
</style>