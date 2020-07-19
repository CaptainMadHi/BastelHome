<template>
  <b-card :title="deviceTitle">
    <component ref="getView" :is="pascalCase(deviceType)" :deviceHash="deviceHash"></component>
    <div class="flex-column">
      <Command
        v-for="(value, key) in commands"
        :key="key"
        :name="key"
        :expectedParams="value"
        :deviceHash="deviceHash"
        @invoke-get="$refs.getView.get()"
      />
    </div>
  </b-card>
</template>

<script>
import { desnakify, pascalCase } from "../utils";
import Command from "./Command";
import MockDevice from "./MockDevice";
import Ledcontrol from "./Ledcontrol";
import SurveillanceCamera from "./SurveillanceCamera";
export default {
  name: "Device",
  components: {
    Command,
    MockDevice,
    Ledcontrol,
    SurveillanceCamera
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