module.exports = {
  head: {
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    ],
    link: [
      { rel: 'stylesheet', href: '/styles/index.css' }
    ]
  },
  build: {
    vendor: ['axios', 'iview']
  }
}