let config = require('~/config')
let baseUrl = config.baseUrl

if (typeof window === 'undefined') {
  baseUrl = config.backendURl
}

const apiList = {
  // 获取文章列表
  getArticles: {
    url: baseUrl + "/articles",
    method: "GET"
  },
  // 获取文章详情
  getArticleDetail: {
    url: baseUrl + "/article/:id",
    method: "GET"
  },

  // 新建文章
  createArticle: {
    url: baseUrl + "/article",
    method: "POST"
  },

  // 更新文章
  updateArticle: {
    url: baseUrl + "/article/:id",
    method: "PUT"
  },

  // 删除文章
  deleteArticle: {
    url: baseUrl + "/article/:id",
    method: "DELETE"
  },

  // 分类列表
  getCates: {
    url: baseUrl + "/categories",
    method: "GET"
  },

  // 登陆
  signin: {
    url: baseUrl + "/user/login",
    method: "POST"
  },

  // todo: 注册

  // 搜索
  searchArticle: {
    url: baseUrl + "/search",
    method: "GET"
  }

}

module.exports = apiList
