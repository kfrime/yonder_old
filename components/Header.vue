<template>
  <div class="app-header">
    <Menu mode="horizontal" :theme="menu_theme" @on-select="navRoute">
      <div class="nav-header">

      <div class="app-logo">
        <a href="/">Yonder</a>
      </div>
      <div class="app-header-right">
        <MenuItem name="home">Home</MenuItem>
        <MenuItem name="archive" >Archive</MenuItem>
        <MenuItem name="about">About</MenuItem>
        <MenuItem name="signup">Sign up</MenuItem>
        <MenuItem name="login">Login</MenuItem>
      </div>
      <div class="app-header-search">
        <Input suffix="ios-search" placeholder="Enter text"/>
      </div>
      </div>
    </Menu>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        menu_theme: 'light'
      }
    },
    methods: {
      navRoute (name) {
        console.log("name:", name)
      }
    }
  }
</script>

<style scoped>
  .app-header {
    position: relative;
    overflow: hidden;
  }
  .nav-header {
    /*margin: 0 15%;*/
  }
  .app-logo {
    position: relative;
    float: left;
    color: rgba(255,255,255,.7);
    font-size: 20px;
    padding: 0 20px;
  }
  .app-header-search{
    position: relative;
    float: right;
    display: inline;
    /*position: center;*/
    padding: 0 20px;
  }
  .app-header-right {
    margin: 0 auto;
    float: right;
    margin-right: 20px;
  }
</style>