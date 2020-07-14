<template>
  <b-card :title="deviceTitle">
    <component :is="pascalCase(device_type)" :deviceHash="device_hash"></component>
    <div class="flex-column">
      <Command
        v-for="(value, key) in commands"
        :key="key"
        :name="key"
        :expectedParams="value"
        :deviceHash="device_hash"
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
    device_hash: String,
    device_name: String,
    device_type: String,
    commands: Object
  },
  computed: {
    deviceTitle() {
      return `${desnakify(this.device_name)} - ${desnakify(this.device_type)}`;
    }
  },
  methods: {
    desnakify,
    pascalCase
  }
};
</script>