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
        <!-- 第一页-->
        <li class="page-item">
          <button
            class="btn page-btn"
            :class="{'item-active': 1 === page.current}"
            @click.prevent="updateArtList(1)"
          >1</button>
        </li>
        <strong v-if="page.pageArr[0] > 2" class="mr-2"> ... </strong>

        <!-- 中间的页码（保持7个） -->
        <li v-for="p in page.pageArr" class="page-item">
          <button
            class="btn page-btn"
            :class="{'item-active': p === page.current}"
            @click.prevent="updateArtList(p)"
          >{{p}}</button>
        </li>

        <!-- 页码表的最后一项跟 最后一页 不相邻时 -->
        <strong v-if="page.pageArr[page.pageArr.length-1] < page.pages-1" class="mr-2"> ... </strong>
        <!-- 最后一页 -->
        <li class="page-item">
          <button
            class="btn page-btn"
            :class="{'item-active': page.pages === page.current}"
            @click.prevent="updateArtList(page.pages)"
          >{{page.pages}}</button>
        </li>
        <!-- 下一页 -->
        <li class="page-item">
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
          pageArr: pageArr,
          pre: null,
          next: null
        }
      }

      let pageArr = []    // 要显示的页码列表
      let start = 2
      let end = page.pages - 1

      // 控制中间所显示页码的范围，page.current 左右各3个
      if (page.pages > 9) {
        if (page.current > 5) {
          start = page.current - 3
        }
        if (page.current < page.pages - 4) {
          end = page.current + 3
        }

        // 中间不够7个页码时，填充满7个
        if (end - start < 7) {
          if (page.current < 5) {
            // 左边满了，填充右边
            end = start + 6
          }
          if (page.current > page.pages - 4) {
            // 右边满了，填充左边
            start = end - 6
          }
        }
      }

      for (var p=start; p <= end; p++) {
        pageArr.push(p)
      }

      // console.log('cur:', page.current, 'pageArr', pageArr)
      page.pageArr = pageArr
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
        search: this.artQuery.search,
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
}
.page-btn {
  color: #222;
  background-color: #fff;
  border: 1px solid #ddd;
}
.page-btn:not(.disabled):active,
.page-btn:not(.disabled):hover,
.item-active {
  box-shadow: none;
  color: #e9ecef;
  background-color: #00a1d6;
  border: 1px solid #00a1d6;
}
.page-btn:focus {
  box-shadow: none;
}
</style>