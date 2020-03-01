const CompressionWebpackPlugin = require('compression-webpack-plugin')
module.exports = {
    productionSourceMap: false,
    outputDir: 'docs',
    publicPath:'./',
    devServer: {
      open: true, //是否自动弹出浏览器页面
      host: "localhost", 
      port: '8080',
      https: false,
      hotOnly: false, 
      proxy: {
          '/api': {
              target: 'http://120.27.192.52:8081', //API服务器的地址
              ws: true,  //代理websockets
              changeOrigin: true, // 虚拟的站点需要更管origin
              pathRewrite: {   //重写路径
                  '^/api': ''
              }
          }
      },
    },
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