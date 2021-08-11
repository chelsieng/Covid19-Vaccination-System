<template>
  <div class="uk-container">
    <form class="uk-form-stacked">
      <div class="uk-margin">
        <label class="uk-form-label uk-text-left" for="query">Enter the sql queries you want to execute</label>
        <div class="uk-form-controls">
          <input class="uk-input" ref="query" id="query" type="text" placeholder="SELECT ___ FROM ___ WHERE ___ ;">
        </div>
      </div>
      <div class="uk-margin">
        <button @click="getQuery(this.$refs.query.value)" type="button" class="uk-button uk-button-default">Submit
        </button>
      </div>
    </form>
    <p class="uk-text-left">{{ this.message }}</p>
    <div class="uk-overflow-auto">
      <table class="uk-table uk-table-striped uk-table-divider">
        <thead>
        <tr>
          <th class="uk-text-center" v-for="field in fields" :key="field">{{ field }}</th>
        </tr>
        </thead>
        <tbody v-for="result in results" :key="result">
        <tr>
          <td class="uk-text-center" v-for="i in fields.length" :key="i">{{ result[i - 1] }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>


</template>

<script>
import axios from "axios";

export default {
  name: "Query",
  data() {
    return {
      message: '',
      fields: "",
      results: ""
    }
  },
  methods: {
    async getQuery(query) {
      await axios
          .get('http://127.0.0.1:8000/' + query + '/')
          .then((response) => {
            console.log(response)
            this.message = "Results: "
            this.fields = response.data["attributes"]
            this.results = response.data["results"];
          })
          .catch((error) => {
            console.log(error.response)
          })
    },
  }
}
</script>

<style scoped>

</style>