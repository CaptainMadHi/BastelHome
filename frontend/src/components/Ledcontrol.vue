<template>
  <div v-if="state" class="flex-row">
    <h5><b-badge :style="{backgroundColor: `rgb(${state.red}, ${state.green}, ${state.blue})`}">color</b-badge></h5>
    <h5>brightness: {{state.brightness}}</h5>
    <h5>animation: {{state.animation || "static"}}</h5>
  </div>
</template>
<script>
import { apiCommand } from "../utils";
export default {
  name: "Ledcontrol",
  props: {
    deviceHash: String
  },
  data: function() {
    return {
      state: undefined
    };
  },
  created() {
    this.get(true);
  },
  methods: {
    async get(repeat=false) {
      try {
        this.state = await apiCommand(this.deviceHash, "get");
        if (repeat) {
          setTimeout(this.get.bind(this, true), 1000);
        }
      } catch (e) {
        this.$bvToast.toast(`Couldn't get data for ledcontrol`, {
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