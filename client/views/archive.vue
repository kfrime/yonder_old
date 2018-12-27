<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <div class="mb-2">
          共<span class="text-danger mx-1">{{archiveResp.count}}</span>篇
        </div>
        <archive-item
          :archive="archive"
          v-for="archive in archiveResp.results"
          :key="archive.year"
        >
        </archive-item>
      </div>

      <!-- sidebar -->
      <div class="col-lg-4 sidebar-module">
        <div class="col-md-offset-2 col-md-10">
          <!-- 主题列表 -->
          <topic-list></topic-list>
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

export default {
  components: {
    ArchiveItem,
    TopicList
  },
  computed: {
    ...mapState(['archiveResp'])
  },
  methods: {
    ...mapActions(['fetchArchivesBy']),
    ...mapMutations(['assignTopicQuery'])
  },
  mounted () {
    const query = {
      name: 'all',
      id: null
    }
    this.fetchArchivesBy(query)
    this.assignTopicQuery(query)
    // console.log('archives:', this.archiveResp)
  }
}
</script>


