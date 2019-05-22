<template>
  <div class="app-header">
    <Menu mode="horizontal" :theme="menu_theme" @on-select="navRoute">
      <div class="app-logo">
        <a href="/">Yonder</a>
      </div>
      <!--<div class="app-header-left">-->
      <div>
        <MenuItem name="home">Home</MenuItem>
        <MenuItem name="archive" >Archive</MenuItem>
        <MenuItem name="about">About</MenuItem>
      </div>

      <div class="app-header-search">
        <Input suffix="ios-search" placeholder="search"/>
      </div>
      <div class="app-header-right">
        <MenuItem name="signup">Sign up</MenuItem>
        <MenuItem name="signin">Sign in</MenuItem>
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
        switch (name) {
          case 'home':
            this.$router.push("/")
            break
          case 'archive':
            this.$router.push("/archive")
            break
          case 'about':
            this.$router.push("/about")
            break
          case 'signup':
            this.$router.push("/signup")
            break
          case 'signin':
            this.$router.push("/signin")
            break
          default:
            // todo: page not found
            console.log("page not found")
        }

      }
    }
  }
</script>

<style scoped>
  .app-header {
    position: relative;
    overflow: hidden;
  }
  .app-logo {
    position: relative;
    float: left;
    color: rgba(255,255,255,.7);
    font-size: 20px;
    padding: 0 40px;
  }
  .app-header-search{
    position: relative;
    float: left;
    /*position: center;*/
    padding: 0 20px;
  }
  .app-header-right {
    margin: 0 auto;
    float: right;
    margin-right: 20px;
  }
</style>