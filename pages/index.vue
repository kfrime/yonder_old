<template>
  <Menu mode="horizontal" :theme="menu_theme">
    <MenuItem name="home">Home</MenuItem>
    <MenuItem name="archive">Archive</MenuItem>
    <MenuItem name="about">About</MenuItem>
    <MenuItem name="search">
      <div>
        <Input suffix="ios-search" placeholder="Enter text" style="width: auto" />
      </div>
    </MenuItem>
  </Menu>
</template>

<script>
  export default {
    data () {
      return {
        menu_theme: 'light'
      }
    }
  }
</script>