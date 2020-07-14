<template>
  <b-card no-body>
    <b-card-header @click="shouldCollapseOpen">
      <div class="flex-row-between">
        <h5>{{desnakify(name)}}</h5>
        <b-button
          @click.stop="sendCommand()"
          variant="success"
          class="flex-shrink-0"
          :disabled="!paramsIsOk"
        >send command</b-button>
      </div>
    </b-card-header>
    <b-collapse v-model="collapseOpen" accordion="accordion">
      <b-card-body class="flex-column">
        <div v-for="(value, key) in expectedParams" :key="key" class="flex-row">
          <label class="flex-shrink-0">{{desnakify(key)}}</label>
          <b-form-input
            class="input-medium"
            v-if="value === 'string'"
            type="text"
            v-model="params[key]"
          ></b-form-input>
          <b-form-input v-else-if="value === 'number'" type="number" v-model.number="params[key]"></b-form-input>
          <b-form-checkbox v-else-if="value === 'boolean'" switch v-model="params[key]"></b-form-checkbox>
        </div>
      </b-card-body>
    </b-collapse>
  </b-card>
</template>

<script>
import { desnakify } from "../utils";
export default {
  name: "Command",
  props: {
    name: String,
    expectedParams: Object
  },
  data: function() {
    return {
      params: {},
      collapseOpenedOnce: false,
      collapseOpen: false
    };
  },
  computed: {
    paramsIsOk: function() {
      if (!this.expectedParams) {
        return false;
      }
      if (Object.keys(this.expectedParams).length === 0) {
        return true;
      }
      for (const key in this.expectedParams) {
        if (typeof this.params[key] !== this.expectedParams[key]) {
          return false;
        }
      }
      return this.collapseOpenedOnce;
    }
  },
  methods: {
    desnakify,
    shouldCollapseOpen(event) {
      if (Object.keys(this.expectedParams).length === 0) {
        return;
      }
      this.collapseOpen = !this.collapseOpen;
      this.collapseOpenedOnce = true;
    },
    sendCommand() {
      alert(1);
    }
  },
  watch: {
    expectedParams: {
      immediate: true,
      deep: true,
      handler: function() {
        for (const key in this.expectedParams) {
          switch (this.expectedParams[key]) {
            case "string":
              this.$set(this.params, key, "");
              break;
            case "number":
              this.$set(this.params, key, 0);
              break;
            case "boolean":
              this.$set(this.params, key, false);
              break;
          }
        }
      }
    }
  }
};
</script>

<style scoped>
</style>