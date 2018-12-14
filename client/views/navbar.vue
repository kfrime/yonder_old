<template>
  <div class="navbar navbar-expand-md navbar-light bg-light py-md-1 navbar-extra" role="navigation">
    <div class="container">
      <a class="navbar-brand d-md-none d-lg-block" href="#">
        <span class="fa fa-snowflake-o"><span class="ml-1">Blog</span></span>
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item pr-2 active">
            <a class="nav-link" href="#">首页<span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item pr-2">
            <a class="nav-link" href="#">归档</a>
          </li>
          <li class="nav-item pr-2">
            <a class="nav-link" href="#">关于</a>
          </li>
        </ul>

        <!-- 搜索框 -->
        <form class="navbar-form" role="search">
          <input type="text" class="form-control py-0 search-bar" placeholder="搜索">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {

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
