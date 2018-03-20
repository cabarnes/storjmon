const merge = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
  mode: 'development',
  resolve: {
    alias: {
      vue: 'vue/dist/vue'
    }
  },
  devtool: 'inline-source-map',
});
