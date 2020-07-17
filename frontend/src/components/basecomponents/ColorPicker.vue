<template>
  <Chrome v-model="val" disable-alpha />
</template>

<script>
import { Chrome } from "vue-color";
export default {
  name: "ColorPicker",
  components: { Chrome },
  props: ["value"],
  data: function() {
    return {
      val: "#000000"
    };
  },
  watch: {
    value(newValue) {
      if (!newValue) {
        this.val = "#000000";
      } else {
        this.val = `#${newValue.toString(16)}`;
      }
    },
    val: {
      immediate: true,
      handler(newValue) {
        let rgbString = newValue.hex || newValue;
        rgbString = rgbString.substr(1);
        this.$emit("input", parseInt(`0x${rgbString}`));
      }
    }
  }
};
</script>