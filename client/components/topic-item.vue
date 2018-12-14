<template>
  <div class="sidebar-item">
    <a href="#" class="btn round-btn sidebar-btn topic-btn">
      <span class="f-15">{{topic.name}}</span>
      <span class="badge f-12">{{topic.total}}</span>
      <!--<span class="badge f-12">12345</span>-->
    </a>
  </div>
</template>

<script>
export default {
  props: ['topic']
}
</script>

<style>
.topic-btn .badge {
  background: #30908d;
}
</style>
