<template>
  <div class="sidebar-item">
    <a href="#" class="btn round-btn sidebar-btn">
      <span class="f-15">{{topic.name}}</span>
      <span class="badge f-12">{{topic.total}}</span>
    </a>
  </div>
</template>

<script>
export default {
  props: ['topic']
}
</script>
