<template>
  <div class="cate-cell">
    <Card>
      <p slot="title" class="cate-card-title">文章分类</p>
      <ButtonGroup slot="extra" v-if="isAdmin">
        <Button :size="buttonSize"><Icon type="ios-code" /></Button>
      </ButtonGroup>

      <cate-item
        v-for="cate in cates"
        :cate="cate"
        :key="cate.ID"
      >
      </cate-item>
    </Card>
  </div>
</template>

<script>
  import CateItem from '~/components/CateItem'

  export default {
    data () {
      return {
        cates: this.$store.state.cates || [],
        isAdmin: this.$store.state.isAdmin || false,
        buttonSize: "small"
      }
    },
    components: {
      'cate-item': CateItem
    }
  }
</script>

<style scoped>
  .cate-cell {
    padding: 8px;
  }
  .cate-card-title {
    font-size: 16px;
    font-weight: bold;
  }
</style>