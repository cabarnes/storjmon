import Vue from 'vue';
import VueResource from 'vue-resource';
Vue.use(VueResource);

import InfoItem from '../components/InfoItem.vue';
import NodeSetting from '../components/NodeSetting.vue';

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
  components: {
    NodeSetting,
  },
  methods: {
    'getInfo': function getInfo() {
      var _this = this;
      _this.$children[0].errorMessage = '';
      infoDisplay.info = null;

      this.$http.get(contactsUrl + _this.$children[0].nodeId)
        .then(function (response) {
          infoDisplay.info = response.data;
        })
        .catch(function (error) {
          _this.$children[0].errorMessage = _this.$children[0].nodeId + ': ' + error.statusText;
        });
    }
  },
});
