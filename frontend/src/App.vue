<template>
  <div id="app">
    <b-container style="max-width: 960px;">
      <h1 class="page-header">BastelHome</h1>
      <div v-if="devices && deviceTypes">
        <Device
          v-for="(device, deviceHash) in devices"
          :key="deviceHash"
          :deviceName="device.device_name"
          :deviceType="device.device_type"
          :deviceHash="deviceHash"
          :commands="filterCommands(deviceTypes[device.device_type])"
        />
      </div>
      <div v-else class="text-center">
        <b-spinner></b-spinner>
      </div>
    </b-container>
  </div>
</template>

<script>
import { apiGetDevices, apiGetDeviceTypes } from "./utils";
import Device from "./components/Device";

export default {
  name: "App",
  components: {
    Device
  },
  data: function() {
    return {
      devices: null,
      deviceTypes: null
    };
  },
  created() {
    this.getDeviceTypes();
    this.getDevices();
  },
  methods: {
    filterCommands(commands) {
      if (!commands) return {};
      const commandsClone = JSON.parse(JSON.stringify(commands));
      delete commandsClone.get;
      return commandsClone;
    },
    async getDeviceTypes() {
      try {
        this.deviceTypes = await apiGetDeviceTypes();
      } catch (e) {
        this.$bvToast.toast("Couldn't get device type data", {
          title: "Connection Error",
          variant: "danger",
          solid: true,
          toaster: "b-toaster-bottom-center"
        });
        console.log(e);
      }
    },
    async getDevices() {
      try {
        this.devices = await apiGetDevices();
      } catch (e) {
        this.$bvToast.toast("Couldn't get device data", {
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

<style>
h1 {
  text-align: center;
  margin-bottom: 2.5rem !important;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

.flex-row {
  display: flex;
  align-items: baseline;
}

.flex-row-between {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.flex-row > :not(:last-child),
.flex-row-between > :not(:last-child) {
  margin-right: 1rem;
}

.flex-shrink-0 {
  flex-shrink: 0;
}

.flex-column > :not(:last-child) {
  margin-bottom: 1rem;
}
</style>
