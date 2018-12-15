<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 main-module">
        <!-- 分类说明 　-->
        <div v-if="this.cate === 'topic'" class="summary">
          {{this.topic.name}}, {{this.topic.total}}
        </div>
        <div v-else-if="this.cate === 'tag'" class="summary">
          {{this.tag.name}}, {{this.tag.total}}
        </div>

        <!-- 文章列表 -->
        <div class="article-list">
          <article-item
            :article="article"
            v-for="article in articles"
            :key="article.id"
          ></article-item>
        </div>
      </div>

      <div class="col-lg-4 sidebar-module">
        <div class="col-md-offset-2 col-md-10">
          <topic-list></topic-list>
          <tag-list></tag-list>
        </div>
          <!-- 主题列表 -->
          <!--<div class="blog-card topic-list">-->
            <!--<div class="topic-title">Topics</div>-->

            <!--<topic-item-->
              <!--:topic = "topic"-->
              <!--v-for="topic in topics"-->
              <!--:key="topic.id"-->
              <!--@updateArticleListByTopic="updateArticleListByTopic"-->
            <!--&gt;</topic-item>-->
          <!--</div>-->

          <!-- 标签列表 -->
          <!--<div class="blog-card tag-list">-->
            <!--<div class="tag-title">Tags</div>-->

            <!--<tag-item-->
              <!--:tag = "tag"-->
              <!--v-for="tag in tags"-->
              <!--:key="tag.id"-->
              <!--@updateArticleListByTag="updateArticleListByTag"-->
            <!--&gt;</tag-item>-->
          <!--</div>-->
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ArticleItem from '../components/article-item.vue'
import TopicList from '../components/topics/topic-list.vue'
import TagList from '../components/tags/tag-list.vue'

export default {
  components: {
    ArticleItem,
    TopicList,
    TagList
  },
  computed: {
    ...mapState(['articles'])
  },
  data () {
    return {
      cate: '',
      topic: null,
      tag: null
    }
  },
  mounted () {
    this.fetchAllArticles()
    console.log('articles', this.articles)
  },
  methods: {
    ...mapActions([
      'fetchAllArticles',
      'fetchArticlesByTopic',
      'fetchArticlesByTag'
    ]),
    updateArticleListByTopic (topicId) {
      this.cate = 'topic'
      this.topic = this.topics.filter(topic => topic.id === topicId)[0]
      console.log('topic:', this.topic.name)
      this.fetchArticlesByTopic(topicId)
    },
    updateArticleListByTag (tagId) {
      this.cate = 'tag'
      this.tag = this.tags.filter(tag => tag.id === tagId)[0]
      console.log('tag:', this.tag.name)
      this.fetchArticlesByTag(tagId)
    }
  }
}
</script>
