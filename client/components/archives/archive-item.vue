<template>
  <div class="archive-item mb-2">
    <div class="text-center archive-item-header py-1 mb-1">
      <div class="text-dark">
        {{archive.year}}年（共<span class="text-danger mx-1">{{archive.total}}</span>篇)
      </div>
    </div>
    <ul>
      <li v-for="art in archive.articles" class="archive-article-link py-1">
        <span class="text-secondary">{{art.date}}&nbsp;</span>
        <!--:to="`/articles/${art.id}/${art.slug}`"-->
        <router-link
          :to="{ name: 'detail', params: { id: art.id, slug: art.slug }}"
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
  margin-bottom: 0.5rem;
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