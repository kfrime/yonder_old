<template>
  <div class="sidebar-item">
    <router-link :to="`/tags/${tag.id}/${tag.slug}`" class="btn round-btn sidebar-btn text-info simple-tag">
      <span class="f-15">{{tag.name}}</span>
    </router-link>
  </div>
</template>

<script>
export default {
  props: ['tag'],
}
</script>

<style>
.simple-tag {
}
</style>
