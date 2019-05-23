
const axios = require('axios')
const apiList = require('~/api/api')

function send(key, options) {
  return new Promise( (resolve, reject) => {
    console.log("send request, key:", key)
    console.log("typeof window:", typeof window)
    let apiConf = apiList[key]
    options = options || {}
    apiConf.method = apiConf.method.toLocaleLowerCase()

    let url = apiConf.url
    console.log("url:", url)

    let axiosConf = {
      method: apiConf.method,
      url: url,
      headers: {}
    }

    axios(axiosConf)
      .then( function (response) {
        return resolve(response.data)
      })
      .catch( function (error) {
        return reject(error)
      })
  })
}

const req = {}

for (let key in apiList) {
  if (apiList.hasOwnProperty(key)) {
    req[key] = (options) => {
      return send(key, options)
    }
  }
}

export default req
