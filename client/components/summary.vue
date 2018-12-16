<template>
  <div class="summary">
    <div
      v-if="this.query.name === 'topic'"
      class="topic-summary"
    >
      <h1 class="f-17">文章分类：{{topic.name}}</h1>
    </div>

    <div
      v-else-if="this.query.name === 'tag'"
      class="tag-summary"
    >
      <h1 class="f-17">文章标签：{{tag.name}}</h1>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState(['query', 'topic', 'tag'])
  },
  methods: {
    ...mapActions(['fetchOneTopic', 'fetchOneTag']),
  },
  watch: {
    query: {
      handler () {
        console.log('query:', this.query.name, ',', this.query.id)
        if (this.query.name === 'topic') {
          this.fetchOneTopic(this.query.id)
        } else if (this.query.name === 'tag') {
          this.fetchOneTag(this.query.id)
        }
      }
    }
  }
}
</script>
