<template>
  <header>
    <nav class="navbar navbar-expand-md bg-white fixed-top blog-navbar py-md-0">
      <a class="navbar-brand d-md-none d-lg-block" href="/">
        <i class="fa fa-home mr-1"></i>Home
        <!--<img href="../assets/images/favicon.ico" width="108" height="40" alt="blog"/>-->
      </a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mr-2">
            <!--{% url 'blog:index' as index_url %}-->
            <!--<a class="nav-link py-md-3 {% if request.path == index_url %}active{% endif %}"-->
            <a class="nav-link py-md-3 active"
               href="#"><i class="fa fa-home mr-1"></i>首页
            </a>
          </li>

          <li class="nav-item mr-2">
            <!--{% url 'blog:about' as about_url %}-->
            <!--<a class="nav-link py-md-3 {% if request.path == about_url %}active{% endif %}"-->
            <a class="nav-link py-md-3"
               href="#"><i class="fa fa-anchor mr-1"></i>关于
            </a>
          </li>

          <li class="nav-item mr-2">
            <a class="nav-link py-md-3"
               href="#"><i class="fa fa-diamond mr-1"></i>后台
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>