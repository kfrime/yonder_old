<template>
  <div class="card border-0 rounded-0 px-3 mb-2 mb-md-3" id="tag-card">
    <div class="card-header bg-white px-0">
      <strong><i class="fa fa-tags mr-2 f-17"></i>标签列表</strong>
    </div>

    <div class="card-body px-0 py-3">
      <tag-item
        :tag="tag"
        v-for="tag in tags"
        :key="tag.id"
        @updateArticleListByTag="updateArticleListByTag"
      ></tag-item>
    </div>
  </div>    <!-- end: tag-card -->
</template>

<script>
import { mapActions } from 'vuex'
import TagItem from './tag-item.vue'

export default {
  props: ['tags'],
  components: {
    TagItem
  },
  methods: {
    ...mapActions(['fetchArticlesByTag']),

    updateArticleListByTag (tagId) {
      const curTagId = this.$route.params.id
      if (curTagId === tagId.toString()) {
        return
      }
      this.fetchArticlesByTag(tagId)
    }
  }
  // computed: {
  //   ...mapState(['tags'])
  // },
  // mounted () {
  //   this.fetchAllTags()
  //   // console.log('tags after mounted', this.tags)
  // }
}
</script>
