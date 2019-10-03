<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <div class="archive-header">
          共<span class="text-danger mx-1">{{archiveList.count}}</span>篇
        </div>
        <archive-item
          :archive="archive"
          v-for="archive in archiveList.data"
          :key="archive.year"
        >
        </archive-item>
      </div>

      <!-- sidebar -->
      <div class="col-lg-4 sidebar-module">
        <div class="col-md-offset-2 col-md-10">
           <!--主题列表-->
          <topic-list></topic-list>
          <tag-list></tag-list>
        </div>
      </div>
      <!-- end sidebar -->
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import TopicList from '../components/topics/topic-list.vue'
import ArchiveItem from '../components/archives/archive-item.vue'
import TagList from '../components/tags/tag-list.vue'

export default {
  components: {
    TagList,
    ArchiveItem,
    TopicList
  },
  computed: {
    ...mapState(['archiveList'])
  },
  methods: {
    ...mapActions(['fetchArchivesBy']),
    ...mapMutations(['assignTopicQuery', 'assignTagQuery'])
  },
  mounted () {
    const query = {
      name: 'all',
      id: null
    }
    this.fetchArchivesBy(query)
    this.assignTopicQuery(query)
    this.assignTagQuery(query)
    // console.log('archives:', this.archiveList)
  }
}
</script>

<style>
.archive-header {
  padding: 0.75rem 1rem;
  margin-bottom: 1rem;
  background-color: #e9ecef;
  border-radius: 0.25rem;
}
</style>
