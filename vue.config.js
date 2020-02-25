const CompressionWebpackPlugin = require('compression-webpack-plugin')
module.exports = {
    productionSourceMap: false,
    chainWebpack: config => {
      // ============压缩图片 start============
      config.module
          .rule('images')
          .use('image-webpack-loader')
          .loader('image-webpack-loader')
          .options({ bypassOnDebug: true, limit: 6144 })
          .end()
      // ============压缩图片 end============
    },
    configureWebpack: config => {
      if (process.env.NODE_ENV === 'production') {
        // gzip压缩
        config.plugins.push(
            new CompressionWebpackPlugin({
                algorithm: 'gzip',
                test: /\.(js|css|svg|woff|ttf|json|html)$/,
                threshold: 10240, // 只有大小大于该值的资源会被处理 10240
                minRatio: 0.8, // 只有压缩率小于这个值的资源才会被处理
                deleteOriginalAssets: false // 删除原文件
            })
        )
      }
  }
}