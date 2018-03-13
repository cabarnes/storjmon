import Vue from 'vue';
import VueResource from 'vue-resource';
Vue.use(VueResource);

import InfoItem from '../components/InfoItem.vue';

var infoDisplay = new Vue({
  el: '#infoDisplay',
  components: {
    InfoItem,
  },
  data: {
    info: Object,
  },
});

var nodeSetting = new Vue({
  el: '#nodeSetting',
  data: {
    nodeId: '',
    errorMessage: '',
  },
  methods: {
    'getInfo': function getInfo() {
      var _this = this;
      _this.errorMessage = '';
      infoDisplay.info = null;

      this.$http.get(contactsUrl + this.nodeId)
        .then(function (response) {
          infoDisplay.info = response.data;
        })
        .catch(function (error) {
          _this.errorMessage = this.nodeId + ': ' + error.statusText;
        });
    }
  },
  delimiters: ['[[',']]'],
});
