module.exports = {
  head: {
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    ],
    link: [
      { rel: 'stylesheet', href: '/styles/index.css' },
      { rel: 'stylesheet', href: '/styles/iview-3.4.1.css' }
    ]
  },
  build: {
    vendor: ['axios', 'iview']
  },
  plugins: [
    { src: '~/plugins/iview.js', ssr: true }
    // { src: '~/plugins/iview.js', mode: "server"}
  ]
}