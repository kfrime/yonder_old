<template id="tag-tpl">
  <!--<a href="#" class="tags f-16" title='#'>{{ tag.name }}</a>-->
  <router-link class="tags f-16" :to="`/tag/${tag.id}`">
    <span @click="handleClick">{{tag.name}}</span>
  </router-link>
</template>

<script>
export default {
  props: ['tag'],
  methods: {
    handleClick (e) {
      this.$emit('updateArticleListByTag', this.tag.id)
    }
  }
}
</script>
