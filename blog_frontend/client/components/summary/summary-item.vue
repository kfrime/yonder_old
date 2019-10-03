<template>
  <div class="card-body summary-body">
    <div class="summary-header f-16 pb-1">
      <span class="float-right mb-0 mr-1">共<span class="text-primary mx-2">{{summary.total}}</span>篇</span>
      <span class="">文章分类：<span class="text-info">{{summary.name}}</span></span>
    </div>
    <p class="f-15 mb-1">{{summary.desc}}</p>
  </div>
</template>

<script>
export default {
  props: ['summary']
}
</script>

<style>
.summary-body {
  border: none;
  padding: 0.5rem;
  background: #f4f4f4;
}
.summary-header {
  margin: 0.1rem 0;
}
</style>
