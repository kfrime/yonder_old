<template>
  <div class="sidebar-item">
    <!--:to="`/tags/${tag.id}/${tag.slug}`" -->
    <router-link
      :to="{name: 'tag', params: { id: tag.id, slug: tag.slug }}"
      class="btn round-btn sidebar-btn tag-btn">
      <span class="f-15">{{tag.name}}</span>
      <span class="badge f-12">{{tag.total}}</span>
    </router-link>
  </div>
</template>

<script>
export default {
  props: ['tag'],
}
</script>

<style>

.tag-btn .badge {
  background: #e09c3b;
}
</style>