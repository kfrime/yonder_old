<template>
  <div>
    <app-header />
    <div class="app-container">
      <!-- 间隔16px -->
      <Row :gutter="32">
        <!--<Col span="3">a</Col>-->
        <Col span="16">
          <nuxt />
        </Col>
        <Col span="8">
          <app-sidebar />
        </Col>
        <!--<Col span="3">a</Col>-->
      </Row>
    </div>
  </div>
</template>

<script>
  import Header from '~/components/Header'
  import Sidebar from '~/components/Sidebar'

  export default {
    components: {
      'app-header': Header,
      'app-sidebar': Sidebar
    }
  }
</script>

<style scoped>
  .app-container {
    width: 1080px;
    margin: 20px auto;
    min-height: 300px;
  }
</style>
