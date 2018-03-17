<template>
  <table class="table">
    <tbody>
      <tr is="info-item"
          v-for="(value, attribute, index) in info"
          v-bind:key="index"
          v-bind:attribute="attribute"
          v-bind:value="value">
      </tr>
    </tbody>
  </table>
</template>

<script>
  import InfoItem from '../components/InfoItem.vue';

  export default {
    name: 'info-list',
    components: {
      'info-item': InfoItem,
    },
    data() {
      return {
        info: null,
      };
    }
  }
</script>
