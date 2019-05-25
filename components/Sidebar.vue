<template>
  <div class="cate-card">
    <!--
    { "ID": 1, "CreatedAt": "2019-05-03T18:46:33+08:00", "UpdatedAt": "2019-05-03T18:46:33+08:00",
     "DeletedAt": null, "Name": "lua" }
     -->
    <div class="cate-card-title">
      <p>文章分类</p>
    </div>
      <Button type="default" shape="circle" class="cate-card-item"
        v-for="cate in cates"
        :cate="cate"
        :key="cate.ID"
      >
        <span class="cate-name">{{cate.Name}}</span>
        <div class="count-badge">
          <!-- Badge, Tag, Button -->
          <!-- type: success、primary、normal、error、warning、info	 -->
          <!-- todo: 该分类下的文章总数 -->
          <Badge type="normal" :count="10"></Badge>
        </div>
      </Button>
  </div>
</template>

<script>
  // import CateItem from '~/components/CateItem'

  export default {
    data () {
      return {
        cates: this.$store.state.cates || [],
        buttonSize: "small"
      }
    },
    components: {
      // 'cate-item': CateItem
    }
  }
</script>

<style scoped>
  .cate-card {
    padding: 8px;
  }
  .cate-card-title {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 8px;
  }
  .cate-card-item {
    margin: 5px 8px;
  }
  .cate-name{
    position: relative;
    display: inline-block;
    font-size: 14px;
  }
  .count-badge {
    margin-left: 10px;
    float: right;
  }
</style>