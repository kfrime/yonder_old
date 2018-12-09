<template>
  <div class="media article-list-item">
    <div class="text-body mb-3">
      <div class="text-muted f-12">
        <span>{{article.author.name}} 创建于：{{article.ctime}}</span>
      </div>
      <a class="title f-15 mb-1" href="#">{{article.title}}</a>
      <p class="d-none d-sm-block mb-1 f-13">{{article.summary}}</p>
      <div class="text-muted f-12">
        <a class="topic" href="#" title="主题">{{article.topic.name}}</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['article']
}
</script>

<style>
.title {
  color: #035fb5;
}
.topic {
  color: #a22b16;
}
</style>