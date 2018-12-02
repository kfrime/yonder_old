<template>
  <div class="card border-0 rounded-0 px-3 mb-2 mb-md-3" id="tag-card">
    <div class="card-header bg-white px-0">
      <strong><i class="fa fa-tags mr-2 f-17"></i>标签列表</strong>
    </div>

    <div class="card-body px-0 py-3">
      <tag-item :tag="tag" v-for="tag in tags" :key="tag.id"></tag-item>
    </div>
  </div>    <!-- end: tag-card -->
</template>

<script>
import { mapState, mapActions } from 'vuex'
import TagItem from './tag-item.vue'

export default {
  components: {
    TagItem
  },
  computed: {
    ...mapState(['tags'])
  },
  methods: {
    ...mapActions(['fetchAllTags'])
  },
  mounted () {
    this.fetchAllTags()
    // console.log('tags after mounted', this.tags)
  }
}
</script>
