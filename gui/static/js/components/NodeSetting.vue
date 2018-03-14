<template>
  <form>
    <div class="form-group">
      <label for="nodeId">Node ID</label>
      <input type="text" class="form-control" v-model="nodeId" placeholder="Enter Node ID">
    </div>
    <div>
      <span v-if="errorMessage" class="error text-danger">{{ errorMessage }}</span>
    </div>
    <button v-on:click="getInfo" type="button" class="btn btn-primary">Update</button>
  </form>
</template>

<script>
  export default {
    data: function() {
      return {
        nodeId: '',
        errorMessage: '',
      }
    },
    methods: {
      'getInfo': function getInfo() {
        this.$emit('get-info');
      }
    }
  }
</script>
