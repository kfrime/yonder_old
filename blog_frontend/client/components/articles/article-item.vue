<template>
  <div class="article-list-item">
    <div class="card article-card">
      <div class="card-body">
        <div class="text-muted f-12">
          <span>
            <i class="fas fa-user mx-1"></i>{{article.author.name}}<i class="mr-1"></i>
            <i class="far fa-calendar-check mx-1"></i>{{article.ctime}}
          </span>
        </div>
        <!--:to="`/articles/${article.id}/${article.slug}`"-->
        <router-link
          :to="{name: 'detail', params: { id: article.id, slug: article.slug }}"
          class="card-title card-link f-16 article-title"
        >{{article.title}}</router-link>
        <p class="card-text my-0">{{article.summary}}</p>
        <div class="article-topic text-muted f-12 py-md-0">
          <!--<router-link :to="`/topics/${article.topic.id}/${article.topic.slug}`" -->
          <router-link
            :to="{name: 'topic', params: { id: article.topic.id, slug: article.topic.slug }}"
            title="主题" class="card-link article-topic">
            <i class="fas fa-book mx-1"></i>{{article.topic.name}}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['article'],
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
.article-card:hover {
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.275);
}
.article-card .card-body {
  padding: 0.5rem;
}
.article-title {
  color: #00a1d6;
}
.article-topic {
  color: #00928e;
  /*color: #3ea943db;*/
}
</style>
