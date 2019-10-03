<template>
  <div class="card summary">
    <div v-if="this.query.name === 'topic'" class="card-body summary-body summary-topic">
      <div class="summary-header f-16 pb-1">
        <span class="float-right mb-0 mr-1">共<span class="text-primary mx-2">{{topic.total}}</span>篇</span>
        <span class="">文章分类：<span class="text-dark"><strong>{{topic.name}}</strong></span></span>
      </div>
      <p class="f-15 mb-1">{{topic.desc}}</p>
    </div>

    <div v-else-if="this.query.name === 'tag'" class="card-body summary-body summary-tag">
      <div class="summary-header f-16 pb-1">
        <span class="float-right mb-0 mr-1">共<span class="text-primary mx-2">{{tag.total}}</span>篇</span>
        <span class="">文章标签：<span class="text-dark"><strong>{{tag.name}}</strong></span></span>
      </div>
      <p class="f-15 mb-1">{{tag.desc}}</p>
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
        // console.log('query:', this.query.name, ',', this.query.id)
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

<style>
.summary {
  padding-bottom: 1rem;
  border: none;
}
.summary-header {
  margin: 0.1rem 0;
}
.summary-body {
  border-bottom: 2px solid #e9ecef;
  padding: 0.5rem;
}
.summary-topic {
  /*background: #2d658421;*/
}
.summary-tag {
  /*background: #f3ce943b;*/
}
</style>
