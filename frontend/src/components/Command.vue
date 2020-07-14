<template>
  <div>
    <b-card no-body>
      <b-card-header v-b-toggle:[accordionToggle]>
        <div class="flex-row-between">
          <h4>{{desnakify(name)}}</h4>
          <b-button
            @click.stop="sendCommand()"
            variant="success"
            class="flex-shrink-0"
            :disabled="!paramsIsOk"
          >send command</b-button>
        </div>
      </b-card-header>
      <b-collapse :id="accordionToggle" @shown="accordionOpenedOnce = true">
        <b-card-body class="flex-column">
          <div v-for="(paramType, key) in expectedParams" :key="key" class="flex-row">
            <label :for="accordionToggle + key" class="flex-shrink-0">{{desnakify(key)}}</label>
            <b-form-input
              class="input-medium"
              v-if="paramType === 'string'"
              :id="accordionToggle + key"
              :type="computeInputType(paramType)"
              v-model="params[key]"
            ></b-form-input>
            <b-form-input
              v-else-if="paramType === 'number'"
              :id="accordionToggle + key"
              :type="computeInputType(paramType)"
              v-model.number="params[key]"
            ></b-form-input>
            <b-form-checkbox
              v-else-if="paramType === 'boolean'"
              :id="accordionToggle + key"
              switch
              v-model="params[key]"
            ></b-form-checkbox>
          </div>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
import { desnakify } from "../utils";
export default {
  name: "Command",
  props: {
    name: String,
    expectedParams: Object,
    accordionToggle: {
      type: String,
      default: "accordion"
    }
  },
  data: function() {
    return {
      params: {},
      accordionOpenedOnce: false
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
      return this.accordionOpenedOnce;
    }
  },
  methods: {
    desnakify,
    computeInputType(value) {
      if (value === "number") return "number";
      return "text";
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