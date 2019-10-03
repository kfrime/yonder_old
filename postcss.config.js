const autoprefixer = require('autoprefixer')

module.exports = {
    plugins: [
        /* 优化编译后的css代码， 为了浏览器兼容，自动给某些css加上一些前缀 */
        autoprefixer()
    ]
}
