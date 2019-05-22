let config = require('~/config')
let baseUrl = config.baseUrl

const apiList = {
  // 获取文章列表
  getArticles: {
    url: baseUrl + "/articles",
    method: "GET"
  }
}

module.exports = apiList
