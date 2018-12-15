<template>
  <!--<div class="col-md-offset-2 col-md-10">-->
    <div class="tag-list">
      <div class="tag-title">文章标签</div>

      <tag-item
      :tag = "tag"
      v-for="tag in tags"
      :key="tag.id"
      ></tag-item>
    </div>
  <!--</div>-->
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import TagItem from './tag-item.vue'

export default {
  components: {
    TagItem
  },
  computed: {
    ...mapState(['tagResp']),
    ...mapGetters(['tags'])
  },
  methods: {
    ...mapActions(['fetchAllTags'])
  },
  mounted () {
    this.fetchAllTags()
  }
}
</script>

<style>
.tag-list{
  padding: 0.5rem;
}
.tag-title{
  padding-bottom: 0.5rem;
}
</style>
