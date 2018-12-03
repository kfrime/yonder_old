<template id="topic-tpl">
  <li class="list-group-item d-flex justify-content-between align-items-center pr-2 py-2">
    <router-link class="category-item" :to="`/topic/${topic.id}`">
      <span @click="handleClick">{{topic.name}}</span>
    </router-link>
    <!--<a class="category-item" href="#" title="#">{{topic.name}}</a>-->
    <span class="badge text-center" title="当前分类下有1篇文章">{{topic.total}}</span>
  </li>
</template>

<script>
export default {
  props: ['topic'],
  methods: {
    handleClick (e) {
      this.$emit('updateArticleListByTopic', this.topic.id)
    }
  }

}
</script>

