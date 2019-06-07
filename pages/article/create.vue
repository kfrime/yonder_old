<template>
  <div>
    <article-editer
      :user="user"
      :article="article"
      :cates="cates"
    >
    </article-editer>
  </div>
</template>

<script>
  import ArticleEditer from "~/components/artEditer"

  export default {
    data () {
      return {
        user: this.$store.state.user,
        cates: this.$store.state.cates,
        article: null,
      }
    },
    components: {
      "article-editer": ArticleEditer,
    },
    layout: "nosidebar",
    // todo: middleware: ""
  }
</script>