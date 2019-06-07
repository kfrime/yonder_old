<template>
  <div>
    <div class="tool-cell">
      <!--操作按钮-->
      <Card dis-hover v-if="isAdmin">
        <p slot="title" class="card-title">操作</p>
        <ButtonGroup>
          <Button :size="buttonSize" @click="toCreatePage">
            <Icon type="md-create" />
          </Button>
        </ButtonGroup>
      </Card>
    </div>

    <div class="cate-cell">
      <Card dis-hover>
        <p slot="title" class="card-title">文章分类</p>
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
    methods: {
      toCreatePage () {
        this.$router.push("/article/create")
      }
    },
    components: {
      'cate-item': CateItem
    }
  }
</script>

<style scoped>
  .tool-cell {
    /*padding: 8px;*/
  }
  .cate-cell {
    /*padding: 8px;*/
    padding-top: 8px;
  }
  .card-title {
    font-size: 16px;
    font-weight: bold;
  }
</style>