<template>
  <div>
    <h4>Status: {{status || "unknown"}}</h4>
  </div>
</template>
<script>
import { apiQuery } from "../utils";
export default {
  name: "MockDevice",
  props: {
    deviceHash: String
  },
  data: function() {
    return {
      status: undefined
    };
  },
  created() {
    this.getStatus();
  },
  methods: {
    async getStatus() {
      try {
        const response = await apiQuery(this.deviceHash, "get");
        this.status = response.status;
        setTimeout(this.getStatus, 1000);
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>