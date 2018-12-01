<template>
  <div id="app">
    <Header></Header>
    <!--<app-main :articles="articles"></app-main>-->
    <router-link to="/" articles="articles"></router-link>
    <router-view />
  </div>
</template>

<script>
// import { mapState, mapGetters } from 'vuex'
import Header from './views/header.vue'
import AppMain from './views/app-main.vue'

export default {
  components: {
    Header,
    AppMain
  },
  mounted () {
    console.log('vuex store', this.$store)
  }
  // computed: {
  //   ...mapState({
  //     articles: (state) => [state.article, state.article]
  //   }),
  //   ...mapGetters({
  //     text: 'text'
  //   })
  // }
}
</script>
