
/*
This config file tells Vue that we don’t want to output to the default directories.
Instead, we want to specify what goes where.
This will help us when telling Django where our static files are and where our HTML template has been compiled to.
*/
const pages = {
  index: "src/main.js",
};

module.exports ={
  publicPath: 'http://localhost:8080', // base URL
  // publicPath: "/static/vue/",
  outputDir: '../static/dist', // where files will be output
  // outputDir: "./build/static/vue/",
  indexPath: '../../templates/_base_vue.html', // path for the index file
  // indexPath: "../../templates/vue_index.html",

  pages: pages,
};
