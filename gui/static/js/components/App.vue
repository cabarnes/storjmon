<template>
  <div>
    <div id="nodeSetting" class="row">
      <div class="col-md-4">
      </div>
      <div class="col-md-4">
        <node-setting v-on:get-info="getInfo"></node-setting>
      </div>
      <div class="col-md-4">
      </div>
    </div>
    <div id="infoDisplay" class="row">
      <div class="col-md-4">
      </div>
      <div class="col-md-4">
        <info-list></info-list>
      </div>
      <div class="col-md-4">
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue';
  import VueResource from 'vue-resource';
  Vue.use(VueResource);

  import InfoList from '../components/InfoList.vue';
  import NodeSetting from '../components/NodeSetting.vue';

  export default {
    name: 'app',
    components: {
      'node-setting': NodeSetting,
      'info-list': InfoList,
    },
    data () {
      return {
        contactsUrl: '',
      };
    },
    methods: {
      getInfo() {
        var _this = this;
        _this.$children[0].errorMessage = '';
        _this.$children[1].info = null;

        this.$http.get(this.contactsUrl + _this.$children[0].nodeId)
          .then((response) => {
            _this.$children[1].info = response.data;
          })
          .catch((error) => {
            _this.$children[0].errorMessage = _this.$children[0].nodeId + ': ' + error.bodyText;
          });
      }
    },
  }
</script>
