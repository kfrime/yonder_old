<template>
  <div class="container article-detail">
    <div class="row">
      <div class="col-lg-9">
        {{article.title}}
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  props: ['id'],
  computed: {
    ...mapState(['article']),
  },
  methods: {
    ...mapActions(['fetchOneArticle'])
  },
  mounted () {
    this.fetchOneArticle(this.id)
  }
}
</script>
