<template>
  <div>
    <h4>Status: {{status || "unknown"}}</h4>
  </div>
</template>
<script>
import { apiCommand } from "../utils";
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
        const response = await apiCommand(this.deviceHash, "get");
        this.status = response.status;
        setTimeout(this.getStatus, 1000);
      } catch (e) {
        this.$bvToast.toast(`Couldn't get data for mock device`, {
          title: "Connection Error",
          variant: "danger",
          solid: true,
          toaster: "b-toaster-bottom-center"
        });
        console.log(e);
      }
    }
  }
};
</script>