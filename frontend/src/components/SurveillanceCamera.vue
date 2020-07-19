<template>
  <b-img center rounded fluid :src="imgUrl" @load="setTimeout(refreshCacheBuster, 100)"></b-img>
</template>
<script>
import { generateCacheBuster } from "../utils";
export default {
  name: "SurveillanceCamera",
  props: {
    deviceHash: String
  },
  data: function() {
    return {
      cacheBuster: ""
    };
  },
  computed: {
    imgUrl() {
      return `/api/command/${deviceHash}/get?${cacheBuster}`;
    }
  },
  methods: {
    refreshCacheBuster() {
      this.cacheBuster = generateCacheBuster();
    }
  }
};
</script>