<template>
  <div class="article-list-item">
    <div class="card article-card">
      <div class="card-body">
        <div class="text-muted f-12">
          <span>{{article.author.name}} 创建于：{{article.ctime}}</span>
        </div>
        <a href="#" class="card-title card-link f-16 article-title">{{article.title}}</a>
        <p class="card-text my-0">{{article.summary}}</p>
        <div class="text-muted f-12 py-md-0">
          <a class="card-link article-topic" href="#" title="主题">{{article.topic.name}}</a>
        </div>
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
.article-list-item {
  padding-bottom: 0.5rem;
}
.article-card {
  border: none;
  background: #f4f4f4;
}
.card:hover {
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.275);
}
.card .card-body {
  padding: 0.5rem;
}
.article-title {
  color: #00a1d6;
}
.article-topic {
  color: #a22b16;
}
</style>
