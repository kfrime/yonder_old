<template>
  <!-- 暂时没用到本组件 -->
  <!--
  { "ID": 1, "CreatedAt": "2019-05-03T18:46:33+08:00", "UpdatedAt": "2019-05-03T18:46:33+08:00",
   "DeletedAt": null, "Name": "lua" }-->
  <div>
    <Button long type="default" class="cate-card-item">
      <!-- todo: to category page -->
      <span class="cate-name">{{cate.Name}}</span>

      <div class="count-badge">
         <!--Badge, Tag, Button -->
         <!--type: success、primary、normal、error、warning、info	 -->
        <!-- todo: 该分类下的文章总数 -->
        <Badge type="normal" :count="10"></Badge>
      </div>

    </Button>
  </div>
</template>

<script>
  export default {
    props: ["cate"],
    data () {
      return {
        buttonSize: "small"
      }
    }

  }
</script>

<style scoped>
  .cate-card-item {
    /*margin: 5px 8px;*/
    margin-bottom: 5px;
  }
  .cate-name{
    position: relative;
    display: inline-block;
    float: left;
    font-size: 14px;
  }
  .count-badge {
    margin-left: 10px;
    float: right;
  }
</style>