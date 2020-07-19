<template>
  <b-img rounded fluid :src="`/api/command/${deviceHash}/get`"></b-img>
</template>
<script>
export default {
  name: "SurveillanceCamera",
  props: {
    deviceHash: String
  }
};
</script>