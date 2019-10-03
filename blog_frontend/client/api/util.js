// 辅助函数
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
      console.log('resp', resp)
      if (!resp.data) {
        return reject(createError(400, 'no data'))
      }
      resolve(resp)
    }).catch(err => {
      console.log('resp err', err)
      reject(err)
    })
  })
}

export default {
  request,
  createError,
  handleRequest
}
