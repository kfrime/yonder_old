<template>
  <div v-if="page.pages > 1" class="page-module">
    <div class="page-wrap my-2">
      <ul class="pagination">
        <!-- 上一页 -->
        <li class="page-item">
          <button
            class="btn page-btn"
            :class="{'disabled': page.pre === null}"
            @click.prevent="updateArtList(page.current - 1)"
          >
            <span aria-hidden="true">&laquo;</span>
            <span class="sr-only">Previous</span>
          </button>
        </li>

        <!-- 页码 -->
        <li v-for="p in page.pages" class="page-item">
          <button
            class="btn page-btn"
            :class="{'item-active': p === page.current}"
            @click.prevent="updateArtList(p)"
          >{{p}}</button>
        </li>

        <!-- 下一页 -->
        <li class="page-item" >
          <button
            class="btn page-btn"
            :class="{'disabled': page.next === null}"
            @click.prevent="updateArtList(page.current + 1)"
          >
            <span aria-hidden="true">&raquo;</span>
            <span class="sr-only">Next</span>
          </button>
        </li>

      </ul>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState(['artResp', 'artQuery']),
    page () {
      const page = this.artResp.page
      if (page === undefined) {
        return {
          pages: 0,
          pre: null,
          next: null
        }
      }
      return page
    }
  },
  methods: {
    ...mapMutations(['assignArtQuery']),
    updateArtList (page) {
      if (page < 1 || page > this.page.pages || page === this.page.current) {
        return
      }
      this.assignArtQuery({
        name: this.artQuery.name,
        id: this.artQuery.id,
        page: page
      })
    }
  }
}
</script>

<style>
.page-module {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}
.page-wrap .page-item {
  margin-right: 0.5rem;
  /*margin: 0 auto;*/
}
.page-btn {
  color: #222;
  background-color: #fff;
  border: 1px solid #ddd;
}
.page-btn:not(.disabled):focus,
.page-btn:not(.disabled):active,
.page-btn:not(.disabled):hover,
.item-active {
  box-shadow: none;
  color: #e9ecef;
  background-color: #00a1d6;
  border: 1px solid #00a1d6;
}
</style>