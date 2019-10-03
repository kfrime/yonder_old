<template id="navbar-tpl">
  <div class="navbar navbar-expand-md bg-white py-md-0 blog-navbar">
    <div class="container">
      <router-link to="/" class="navbar-brand d-md-none d-lg-block">
        <span class="fa fa-snowflake-o mr-1"> Blog</span>
      </router-link>
      <!--<a class="navbar-brand d-md-none d-lg-block" href="#">首页-->
        <!--<img src="../assets/images/favicon.ico" width="50" height="50" class="img-fluid" alt="首页">-->
      <!--</a>-->
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- 操作按钮 -->
      <div class="collapse navbar-collapse " id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mr-2">
            <router-link to="/" class="nav-link py-md-3"><i class="fa fa-home mr-1"></i>首页
              <span class="sr-only">(current)</span>
            </router-link>
          </li>
          <li class="nav-item mr-2">
            <a class="nav-link py-md-3" href="#"><i class="fa fa-sitemap mr-1"></i>归档</a>
          </li>
          <li class="nav-item mr-2">
            <a class="nav-link py-md-3" href="#"><i class="fa fa-key mr-1"></i>API</a>
          </li>
          <li class="nav-item mr-2 ">
            <a class="nav-link py-md-3" href="#"><i class="fa fa-anchor mr-1"></i>关于</a>
          </li>
        </ul>
        <ul class="navbar-nav navbar-right ">
          <form class="navbar-form" role="search" method="get" id="searchform" action="">
            <div class="input-group">
              <input type="search" name="q" class="form-control rounded-0 f-15" placeholder="搜索" required="True">
              <div class="input-group-btn">
                <button class="btn btn-info rounded-0" type="submit"><i class="fa fa-search"></i></button>
              </div>
            </div><!-- /input-group -->
          </form>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.blog-navbar {
  box-shadow: 0 2px 4px 0 rgba(0,0,0,0.05);
}
</style>
