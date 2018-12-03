<template id="article-tpl">
  <div class="media mb-1 ml-0 mb-sm-2 p-2 p-lg-3 article-list-item">
    <div class="text-body">
      <div class="text-muted mb-2 f-12">
        <span>{{article.author.name}}</span>
        <span><i class="fa fa-calendar-times-o ml-2 mr-1"></i>{{article.ctime}}</span>
      </div>
      <h2 class="mt-0 font-weight-bold text-info f-17">
        <!--<a href="#">{{article.title}}</a>-->
        <router-link :to="`/article/${article.id}`">{{article.title}}</router-link>
      </h2>
      <p class="d-none d-sm-block mb-2 f-15">{{article.summary}}</p>
      <div class="text-muted mb-0 f-12">
        <!--<a class="cate" href="#" title="查看当前分类下更多文章"></a>-->
        <router-link class="cate" :to="`/topic/${article.topic.id}`">
          <i class="fa fa-book mr-1"></i>{{article.topic.name}}
        </router-link>
        <!--<span><i class="fa fa-eye ml-2 mr-1"></i>1356</span>-->
        <!--<a href="#" title="查看文章评论">-->
        <!--<i class="fa fa-comments ml-2 mr-1"></i>33</a>-->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['article']
}
</script>

<style scoped>
/* 用户头像 */
.article-list .avatar {
  width:1.2rem;
  heigth:1.2rem;
  margin-right:.2rem;
  border-radius: 50%;
}

.article-list .media {
  background-color: #fff;
}

.article-list .cate {
  color: #ea6f5a;
}

.article-list .cate:hover {
  color: #17a2b8;
}

.article-list-item {
  padding-top: 15px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}
</style>
