<template>
  <div id="app">
    <b-container v-if="devices && deviceTypes">
      <h1 class="page-header">BastelHome</h1>
      <Device
        v-for="(device, deviceHash) in devices"
        :key="deviceHash"
        :deviceName="device.device_name"
        :deviceType="device.device_type"
        :deviceHash="deviceHash"
        :commands="filterCommands(deviceTypes[device.device_type])"
      />
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
      devices: {
        "test-hash": {
          device_name: "Test Device",
          device_type: "mock_device"
        }
      },
      deviceTypes: {
        mock_device: {
          get: {},
          change_status: {
            new_status: "boolean"
          },
          invert_status: {}
        }
      }
    };
  },
  created() {
    this.getDeviceTypes();
    this.getDevices();
  },
  methods: {
    filterCommands(commands) {
      const commandsClone = JSON.parse(JSON.stringify(commands));
      delete commandsClone.get;
      return commandsClone;
    },
    async getDeviceTypes() {
      try {
        this.deviceTypes = await apiGetDeviceTypes();
      } catch (e) {
        console.log(e);
      }
    },
    async getDevices() {
      try {
        this.deviceTypes = await apiGetDevices();
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
h1 {
  text-align: center;
  margin-bottom: 2.5rem!important;
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
