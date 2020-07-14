<template>
  <div id="app">
    <b-container>
      <Command name="change_value" accordion-toggle="test" :expectedParams="expectedParams" />
    </b-container>
  </div>
</template>

<script>
import Command from "./components/Command";

export default {
  name: "App",
  components: {
    Command
  },
  data: function() {
    return {
      expectedParams: {
        new_status: "number",
        something_else: "boolean"
      }
    };
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
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
