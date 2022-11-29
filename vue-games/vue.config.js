const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: 'http://localhost:8080', // base URL
  outputDir: '../static/dist', // where files will be output
  indexPath: '../../templates/_base_vue.html', // path for the index file

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
})
