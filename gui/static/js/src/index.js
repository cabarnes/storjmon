import Vue from 'vue';

import App from '../components/App.vue';

new Vue({ // eslint-disable-line no-new
  el: '#app',
  components: {
    app: App,
  },
  mounted() {
    this.$children[0].contactsUrl = contactsUrl;
  },
});
