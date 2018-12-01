<template>
  <div class="container">
    <div class="content">author: {{ article.author }}</div>
    <div class="content">title: {{ article.title }}</div>
    <div class="content">summary: {{ article.summary }}</div>
    <div class="content">content: {{ article.content }}</div>
    <div class="text">getter text: {{ text }}</div>
  </div>
</template>

<style lang="stylus" scoped>
  .content, .text{
    text-align center
  }
  .content{
    color #6a1868
  }
</style>
