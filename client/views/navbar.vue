<template>
  <div id="blog-navbar"
       class="navbar navbar-expand-md navbar-light bg-light py-md-1 navbar-extra"
       role="navigation"
  >
    <div class="container">
      <router-link :to="{name: 'home'}" class="navbar-brand d-md-none d-lg-block">
        <span class="far fa-snowflake"><span class="ml-1">Blog</span></span>
      </router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item pr-2 active">
            <router-link :to="{name: 'home'}" class="nav-link">
              <span><i class="fas fa-home mr-1"></i>首页</span>
              <span class="sr-only">(current)</span>
            </router-link>
          </li>
          <li class="nav-item pr-2">
            <router-link :to="{name: 'archive'}" class="nav-link"><i class="fas fa-folder-open mr-1"></i>归档</router-link>
          </li>
          <li class="nav-item pr-2">
            <router-link :to="{name: 'about'}" class="nav-link"><i class="fas fa-paw mr-1"></i>关于</router-link>
          </li>
        </ul>

        <!-- 搜索框 -->
        <div class="navbar-form" role="search">
          <input
            v-model="search"
            type="text"
            class="form-control py-0 search-bar"
            autofocus="autofocus"
            placeholder="搜索"
            @keyup.enter="searchArticles"
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data () {
    return {
      search: ''
    }
  },
  methods: {
    searchArticles (e) {
      const content = e.target.value.trim()
      // console.log('search:', content)
      if (!content) {
        const msg = 'input can not be empty'
        this.$notify({
          content: msg
        })
        return
      }
      e.target.value = ''
      const route = { name: 'search', params: { search: content }}
      this.$router.push(route)
    }
  },
  watch: {
    search: {
      handler () {
        // const route = { name: 'search', params: { search: this.search }}
        // this.$router.push(route)
        // sleep(500)    // 防止输入过快
      }
    }
  }
}
</script>

<style>
  .navbar-extra {
    border-color: #080808;
    margin-bottom: 1rem;
  }
  input.search-bar[type="text"] {
    border-radius: 1020px;
  }
</style>
