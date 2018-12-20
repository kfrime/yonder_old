<template>
  <div aria-label="Page navigation example">
    <ul class="pagination">
      <li class="page-item">
        <a class="page-link" href="#" aria-label="Previous" :disabled="page.pre === null">
          <span aria-hidden="true">&laquo;</span>
          <span class="sr-only">Previous</span>
        </a>
      </li>
      <!-- 页码 -->
      <li
        v-for="p in page.pages"
        class="page-item"
        :disabled="p === page.current"
      >
        <a class="page-link" href="#" @click.prevent="updateArtList(p)">{{p}}</a>
      </li>

      <li class="page-item">
        <a class="page-link" href="#" aria-label="Next" :disabled="page.next === null">
          <span aria-hidden="true">&raquo;</span>
          <span class="sr-only">Next</span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState(['artResp', 'artQuery']),
    ...mapGetters(['page'])
    // page () {
    //   return this.artResp.page
    // }
  },
  methods: {
    ...mapMutations(['assignArtQuery']),
    updateArtList (page) {
      // const query = Object.assign({}, this.artQuery)
      // query.page = page
      this.assignArtQuery({
        name: this.artQuery.name,
        id: this.artQuery.id,
        page: page
      })
    }
  }
}
</script>