<template>
  <div id="app">
    <div class="test">{{ content }}</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      content: 'Hello Vue'
    }
  }
}
</script>

<style lang="stylus" scoped>
#app{
  background-color #999
  color red
  text-align center
}
</style>