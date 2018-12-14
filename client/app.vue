<template>
  <div class="app-main">
    <navbar></navbar>
    <!--<blog></blog>-->
    <router-link to="/"></router-link>
    <router-view />
    <!--<div class="footer">footer</div>-->
  </div>
</template>

<script>
import Navbar from './views/navbar.vue'
import Blog from './views/blog.vue'

export default {
  components: {
    Navbar,
    Blog
  }
}
</script>