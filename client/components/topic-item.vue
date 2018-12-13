<template>
  <div class="topic-item">
    <a href="#" class="btn  round-btn topic-btn">
      <span class="f-15">{{topic.name}}</span>
      <span class="badge">{{topic.total}}</span>
    </a>
    <!--<a href="#" class="btn btn-xs btn-default round-btn topic-btn" title="">-->
      <!--<span class="f-12 text-gray">{{topic.name}}</span>-->
      <!--<span class="badge f-10">{{topic.total}}</span>-->
    <!--</a>-->
  </div>
</template>

<script>
export default {
  props: ['topic']
}
</script>

<style>
  .topic-item {
    margin-bottom: 0.3rem;
  }
  .topic-btn {
    color: #000;
    /*padding: 0.1rem;*/
    /*padding-bottom: 3px;*/
    padding-bottom: 0.1rem;
    padding-top: 0.1rem;
    /*padding-left: 10px;*/
    /*padding-left: 0.75rem;*/
    /*margin-bottom: 5px;*/
    /*margin-right: 2px;*/
    background-color: #fff;
    /*border-color: #ccc;*/
    /*margin-bottom: 0.5rem;*/
  }

  .btn-xs {
    padding: 1px 5px;
    font-size: 12px;
    line-height: 1.5;
    border-radius: 3px;
  }

  /*.btn.btn-default, .btn.btn-default:active, .btn.btn-default:active:focus, .btn.btn-default:focus {*/
    /*border: 1px solid #ddd;*/
  /*}*/

  .round-btn {
    border-radius: 1020px;
  }

  /*.btn-default {*/
    /*color: #333;*/
    /*background-color: #fff;*/
    /*border-color: #ccc;*/
  /*}*/
  /*.btn-default .badge {*/
    /*color: #fff;*/
  /*}*/
  .text-sm {
    font-size: 10px;
  }
  .topic-btn .badge {
    color: #fff;
    background: #17807d;
    border-radius: 1020px;
    padding: 2px;
  }
</style>

