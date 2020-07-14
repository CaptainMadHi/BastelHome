<template>
  <b-card :title="deviceTitle">
    <component :is="device_type" :deviceHash="device_hash"></component>
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
import { desnakify } from "../utils";
import Command from "./Command";
export default {
  name: "Device",
  components: {
    Command
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
    desnakify
  }
};
</script>