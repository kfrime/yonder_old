<template>
  <div class="archive-item">
    <div class="">
      {{archive.year}}（共<span class="text-danger mx-1">{{archive.total}}</span>篇)
    </div>
    <ul>
      <li v-for="art in archive.articles">
        {{art.date}}&nbsp;
        <router-link
          :to="`/articles/${art.id}`"
          class="card-title card-link f-16 article-title"
        >{{art.title}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['archive']
}
</script>

<style>
.article-title {
  color: #00a1d6;
}
</style>