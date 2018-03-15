<template>
  <tr>
    <td>{{ attribute }}</td>
    <td>{{ value }}</td>
  </tr>
</template>

<script>
  export default {
    props: {
      attribute: String,
      value: [String, Number, Boolean],
    },
    data () {
      return {};
    },
  }
</script>
