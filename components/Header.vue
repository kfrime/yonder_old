<template>
  <div class="app-header">
    <Menu mode="horizontal" :theme="menu_theme">
      <div class="app-logo">
        <!--<a href="/">Yonder</a>-->
        <nuxt-link to="/">Yonder</nuxt-link>
      </div>
      <MenuItem name="home">
        <nuxt-link to="/">Home</nuxt-link>
      </MenuItem>
      <MenuItem name="archive">
        <nuxt-link to="/archive">Archive</nuxt-link>
      </MenuItem>
      <MenuItem name="about">About</MenuItem>
      <MenuItem name="search">
        <div>
          <Input suffix="ios-search" placeholder="Enter text" style="width: auto" />
        </div>
      </MenuItem>
      <div class="app-header-right">
        <MenuItem name="signup">Sign up</MenuItem>
        <MenuItem name="login">Login</MenuItem>
      </div>
    </Menu>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        menu_theme: 'dark'
      }
    }
  }
</script>

<style scoped>
  .app-header {
    position: relative;
    /*overflow: hidden;*/
  }
  .app-logo {
    position: relative;
    float: left;
    color: rgba(255,255,255,.7);
    font-size: 20px;
    /*margin-left: 16.2rem;*/
    padding: 0 20px;
  }
  .app-header-right {
    margin: 0 auto;
    float: right;
    margin-right: 20px;
  }
</style>