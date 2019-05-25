<template>
  <!-- 暂时没用到本组件 -->
  <!--
  { "ID": 1, "CreatedAt": "2019-05-03T18:46:33+08:00", "UpdatedAt": "2019-05-03T18:46:33+08:00",
   "DeletedAt": null, "Name": "lua" }-->
  <div>
    <ButtonGroup vertical>
      <Button>{{ar}}</Button>
      <Button icon="logo-twitter"></Button>
      <Button icon="logo-googleplus"></Button>
      <Button icon="logo-tumblr"></Button>
    </ButtonGroup>
    {{cate}}
  </div>
</template>

<script>
  export default {
    props: ["cate"]
  }
</script>