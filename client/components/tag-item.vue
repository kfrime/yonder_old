<template>
  <div class="sidebar-item">
    <a href="#" class="btn round-btn sidebar-btn">
      <span class="f-15">{{tag.name}}</span>
      <span class="badge f-12">{{tag.total}}</span>
    </a>
  </div>
</template>

<script>
export default {
  props: ['tag']
}
</script>
