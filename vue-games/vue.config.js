/*
Here we have set the publicPath, the outputDir, and the indexPath.
This configures where our app will be deployed (http://localhost:8080), where
build files should go when we run npm run build (static/dist), and where our
generated index file should go (templates/_base_vue.html). We also configure
the dev server to output our index.html into its file (writeToDisk) rather
than preserve it in memory. This allows our Django to access it.
*/

module.exports = {
  publicPath: 'http://localhost:8080',
  outputDir: '../static/dist',
  indexPath: '../../templates/_base_vue.html',
};
