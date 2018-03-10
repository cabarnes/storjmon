Vue.component('info-item', {
  props: ['attribute', 'value'],
  template: '<tr><td>[[ attribute ]]</td><td>[[ value ]]</td></tr>',
  delimiters: ['[[',']]'],
})

var infoDisplay = new Vue({
  el: '#infoDisplay',
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
