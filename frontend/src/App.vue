<template>
  <div id="app">
    <b-container>
      <Device device_name="Mein Licht" device_type="some_type" :commands="commands" />
    </b-container>
  </div>
</template>

<script>
import Device from "./components/Device";
import Command from "./components/Command";

export default {
  name: "App",
  components: {
    //Command,
    Device
  },
  data: function() {
    return {
      device: {
        get: {},
        change_status: {
          new_status: "boolean"
        },
        change_status2: {
          new_status: "boolean"
        },
        invert_status: {}
      }
    };
  },
  computed: {
    commands() {
      let { get, ...filteredCommands } = this.device;
      return filteredCommands;
    }
  }
};
</script>

<style>
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
