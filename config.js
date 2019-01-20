const isDev = process.env.NODE_ENV === 'development'

const config = {
  serverUrl: isDev ? 'http://localhost:8000' : 'http://192.168.3.221:8000'
}

module.exports = config
