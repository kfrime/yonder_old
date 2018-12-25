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
  /*
  getAllArticles () {
    return handleRequest(request.get('/api/articles/'))
  },
  getArticleByTag (tagId) {
    return handleRequest(request.get(`/api/articles/?tag=${tagId}`))
  },
  getArticleByTopic (topicId) {
    return handleRequest(request.get(`/api/articles/?topic=${topicId}`))
  },
  getAllTags () {
    return handleRequest(request.get('/api/tags/'))
  },
  getTagByArticleId (id) {
    return handleRequest(request.get(`/api/tags/?article=${id}`))
  },
  */
  getOneArticle (id) {
    return handleRequest(request.get(`/api/articles/${id}/`))
  },
  getTopic (id) {
    return handleRequest(request.get(`/api/topics/${id}/`))
  },
  getTag (id) {
    return handleRequest(request.get(`/api/tags/${id}/`))
  },
  getArticleList(filter, id, search='', page=1) {
    /* filter:
     *  all - 获取所有文章列表
     *  topic - 根据 topic id 筛选文章列表
     *  tag - 根据 tag id 筛选文章列表
     */
    // console.log('getArticleList, filter:', filter, 'id:', id, 'page:', page)
    let url = `/api/articles/`
    let params = []

    if (filter === 'all') {
      /* do nothing */              // `/api/articles/`
    } else if (filter === 'topic') {
      params.push(`topic=${id}`)    // `/api/articles/?topic=${id}`
    } else if (filter === 'tag') {
      params.push(`tag=${id}`)      // `/api/articles/?tag=${id}`
    } else {
      // todo: thrown error
      console.log(`unknown filter type: ${filter}`)
      return
    }

    if (search !== '' && typeof search !== "undefined") {
      params.push(`search=${search}`)
    }

    if (page !== 1 && typeof page !== "undefined") {
      params.push(`page=${page}`)
    }

    // console.log('params:', params)
    if (params.length > 0) {
      url = url + '?' + params.shift()
      for (var p of params) {
        url = url + '&' + p     // eg: `/api/articles/?topic=1&page=2`
      }
    }

    // console.log('url:', url)
    const resp = handleRequest(request.get(url))
    return resp
  },
  getTopicList (filter, id) {
    /* filter:
     *  all - 获取所有主题列表
     */
    let baseUrl = '/api/topics/'
    let url = ''
    let query = ''

    if (filter === 'all') {
      query = ''
    } else {
      // todo: thrown error
      console.log(`unknown filter type: ${filter}`)
    }
    url = baseUrl + query
    const resp = handleRequest(request.get(url))
    return resp
  },
  getTagList (filter, id) {
    /* filter:
     *  all - 获取所有标签列表
     *  article - 根据 article id 筛选标签列表
     */
    let baseUrl = '/api/tags/'
    let url = ''
    let query = ''

    if (filter === 'all') {
      query = ''              // `/api/tags/`
    } else if (filter === 'article') {
      query = `?article=${id}`  // `/api/tags/?article=${id}`
    } else {
      // todo: thrown error
      console.log(`unknown filter type: ${filter}`)
    }
    url = baseUrl + query
    const resp = handleRequest(request.get(url))
    return resp
  },
  searchArticles (value, page=1) {
    let url = `/api/articles/search/`
    let params = []

    if (value !== '' && typeof value !== "undefined") {
      params.push(`q=${value}`)
    }

    if (page !== 1 && typeof page !== "undefined") {
      params.push(`page=${page}`)
    }

    // console.log('params:', params)
    if (params.length > 0) {
      url = url + '?' + params.shift()
      for (var p of params) {
        url = url + '&' + p     // eg: `/api/articles/?topic=1&page=2`
      }
    }

    // console.log('url:', url)
    const resp = handleRequest(request.get(url))
    return resp
  },
  getArchives (filter, id) {
    /* filter:
     *  all - 获取所有主题列表
     */
    let baseUrl = '/api/archives/'
    let url = ''
    let query = ''

    if (filter === 'all') {
      query = ''              // `/api/archives/`
    } else if (filter === 'topic') {
      query = `?topic=${id}`  // `/api/archives/?topic=${id}`
    } else {
      // todo: thrown error
      console.log(`unknown filter type: ${filter}`)
    }
    url = baseUrl + query
    const resp = handleRequest(request.get(url))
    return resp
  },
}
