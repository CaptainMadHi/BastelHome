<template>
  <b-card :title="deviceTitle">
    <component :is="pascalCase(deviceType)" :deviceHash="deviceHash"></component>
    <div class="flex-column">
      <Command
        v-for="(value, key) in commands"
        :key="key"
        :name="key"
        :expectedParams="value"
        :deviceHash="deviceHash"
      />
    </div>
  </b-card>
</template>

<script>
import { desnakify, pascalCase } from "../utils";
import Command from "./Command";
import MockDevice from "./MockDevice";
export default {
  name: "Device",
  components: {
    Command,
    MockDevice
  },
  props: {
    deviceHash: String,
    deviceName: String,
    deviceType: String,
    commands: Object
  },
  computed: {
    deviceTitle() {
      return `${desnakify(this.deviceName)} - ${desnakify(this.deviceType)}`;
    }
  },
  methods: {
    desnakify,
    pascalCase
  }
};
</script>