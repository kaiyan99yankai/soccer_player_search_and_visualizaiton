module.exports = {
  outputDir: "dist",
  assetsDir: "static",
  indexPath: "index.html",
  publicPath: "/",
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
};