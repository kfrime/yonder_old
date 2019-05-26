<template>
  <div class="cate-card">
    <!--
    { "ID": 1, "CreatedAt": "2019-05-03T18:46:33+08:00", "UpdatedAt": "2019-05-03T18:46:33+08:00",
     "DeletedAt": null, "Name": "lua" }
     -->
    <div class="cate-card-title">
      <p>文章分类</p>
    </div>
    <cate-item
      v-for="cate in cates"
      :cate="cate"
      :key="cate.ID"
    >
    </cate-item>
  </div>
</template>

<script>
  import CateItem from '~/components/CateItem'

  export default {
    data () {
      return {
        cates: this.$store.state.cates || [],
      }
    },
    components: {
      'cate-item': CateItem
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
    margin: 0 5px 8px 5px;
    /*margin-bottom: 8px;*/
  }

</style>