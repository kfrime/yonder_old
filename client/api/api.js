// import { request, createError, handleRequest } from './util'
const axios = require('axios')

const request = axios.create({
  baseURL: 'http://localhost:8000/'
})

const createError = (code, resp) => {
  const err = new Error(resp.message)
  err.code = code
  return err
}

const handleRequest = (request) => {
  return new Promise((resolve, reject) => {
    request.then(resp => {
      // console.log('resp', resp)
      if (!resp.data) {
        return reject(createError(400, 'no data'))
      }
      resolve(resp.data)
    }).catch(err => {
      console.log('resp err', err)
      reject(err)
    })
  })
}

export default {
  getAllArticles () {
    return handleRequest(request.get('/api/articles/'))
  },
  getArticle (id) {
    return handleRequest(request.get(`/api/articles/${id}/`))
  },
  getArticleByTopic (topicId) {
    return handleRequest(request.get(`/api/articles/?topic=${topicId}`))
  },
  getAllTopics () {
    return handleRequest(request.get('/api/topics/'))
  },
  getTopic (id) {
    return handleRequest(request.get(`/api/topics/${id}/`))
  },
  getAllTags () {
    return handleRequest(request.get('/api/tags/'))
  },
  getTag (id) {
    return handleRequest(request.get(`/api/tags/${id}/`))
  },
  getTagByArticleId (id) {
    return handleRequest(request.get(`/api/tags/?article=${id}`))
  },
  getArticleByTag (tagId) {
    return handleRequest(request.get(`/api/articles/?tag=${tagId}`))
  }
}
