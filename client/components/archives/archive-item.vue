<template>
  <div class="archive-item mb-2">
    <div class="text-center archive-item-header mb-2">
      <div class="my-1 text-dark">
        {{archive.year}}年（共<span class="text-danger mx-1">{{archive.total}}</span>篇)
      </div>
    </div>
    <ul>
      <li v-for="art in archive.articles" class="archive-article-link">
        <span class="text-secondary">{{art.date}}&nbsp;</span>
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
.archive-item {
  border: none;
  background: #f4f4f4;
}
.archive-item-header {
  border-bottom: 2px solid #e9ecef;
}
.archive-article-link {

}
.archive-item ul {
  list-style: none;
}

.archive-item ul li::before {
  content: "\2022";
  color: #6c757d;
  display: inline-block;
  width: 1em;
  margin-left: -1em;
}
.article-title {
  color: #00a1d6;
}
</style>