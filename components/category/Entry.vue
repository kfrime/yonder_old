<template>
  <div>
    <Card>
      {{cate.Name}}
      <ButtonGroup class="cate-tool">
        <Button :size="buttonSize" @click="toEditPage"><Icon type="ios-code" /></Button>
        <Button :size="buttonSize" @click="deleteConfirm = true"><Icon type="ios-close" /></Button>
        <Modal
          v-model="deleteConfirm"
          title="delete or not ?"
          @on-ok="deleteCategory"
        >
          <p>delete category</p>
        </Modal>
      </ButtonGroup>
    </Card>
  </div>
</template>

<script>
  export default {
    props: ["cate"],
    data () {
      return {
        buttonSize: "small",
        edit: false,
        deleteConfirm: false,
      }
    },
    methods: {
      toEditPage () {
        console.log("update category")
      },
      deleteCategory () {
        console.log("delete category")
      },
    },
  }
</script>

<style scoped>
  .cate-tool {
    float: right;
  }
</style>
