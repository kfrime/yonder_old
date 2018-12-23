<template>
  <div class="navbar navbar-expand-md navbar-light bg-light py-md-1 navbar-extra" role="navigation">
    <div class="container">
      <router-link to="/" class="navbar-brand d-md-none d-lg-block">
        <span class="fa fa-snowflake-o"><span class="ml-1">Blog</span></span>
      </router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item pr-2 active">
            <router-link to="/" class="nav-link">
              <span>首页</span>
              <span class="sr-only">(current)</span>
            </router-link>
          </li>
          <li class="nav-item pr-2">
            <a class="nav-link" href="#">归档</a>
          </li>
          <li class="nav-item pr-2">
            <a class="nav-link" href="#">关于</a>
          </li>
        </ul>

        <!-- 搜索框 -->
        <div class="navbar-form" role="search">
          <input
            type="text"
            class="form-control py-0 search-bar"
            autofocus="autofocus"
            placeholder="搜索"
            @keyup.enter.prevent="searchArticles"
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  methods: {
    searchArticles (e) {
      const content = e.target.value.trim()
      // console.log('search:', content)
      if (!content) {
        console.log('input can not be empty')
        return
      }
      e.target.value = ''
      const route = `/articles/search/${content}`
      this.$router.push(route)
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
