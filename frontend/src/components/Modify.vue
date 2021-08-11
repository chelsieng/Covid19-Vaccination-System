<template>
  <div class="uk-container">
    <h2>{{ this.name }}</h2>
    <p>Total records: {{ this.results.length }}</p>
    <div class="uk-align-left "><a href="#" class="uk-icon-button uk-text-primary" uk-icon="plus"
                                   uk-tooltip="title: Create new data"></a></div>
    <div class="uk-overflow-auto">
      <table class="uk-table uk-table-hover uk-table-divider">
        <thead>
        <tr>
          <th class="uk-text-center" v-for="field in fields" :key="field">{{ field }}</th>
          <th></th>
          <th></th>
        </tr>
        </thead>
        <tbody v-for="result in results" :key="result">
        <tr>
          <td class="uk-text-center" v-for="i in fields.length" :key="i">{{ result[i - 1] }}</td>
          <td><a @click="edit(result)" ref="edit" href="#" class="uk-icon-button uk-text-primary" uk-icon="pencil"
                 uk-tooltip="title: Edit data"></a></td>
          <td><a @click="remove(result)" ref="delete" href="#" class="uk-icon-button uk-text-danger" uk-icon="trash"
                 uk-tooltip="title: Delete record" uk-toggle="target: #modal"></a></td>
        </tr>
        </tbody>
      </table>
    </div>
    <!--    modal-->
    <div id="modal" uk-modal="bg-close: false">
      <div class="uk-modal-dialog uk-modal-body uk-text-center">
          <h3 class="uk-text-center">{{this.msg }}</h3>
        <p class="uk-text-center">
          <button class="uk-button uk-button-primary" type="button" @click="refresh()">Refresh</button>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Modify",
  props: ['table'],
  data() {
    return {
      name: "Table name",
      msg: "",
      fields: "",
      results: "",
      sql: "",
    }
  },
  mounted() {
    if (this.table) {
      this.name = this.table
      this.getTables(this.name)
    }
  },
  methods: {
    async getTables(name) {
      await axios
          .get('http://127.0.0.1:8000/select * from ' + name + '/')
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
    async add() {

    },
    async edit(r) {
      console.log(r)
    },
    async remove(record) {
      this.sql = "delete from " + this.name + " where ";
      for (let i = 0; i < this.fields.length; i++) {
        if (typeof record[i] == 'number') {
          console.log(record[i] + "is a numberr")
          if ((i) === (this.fields.length - 1)) {
            console.log(i)
            console.log(this.fields.length)
            this.sql += this.name + "." + this.fields[i] + "=" + record[i] + ";"
          } else {
            this.sql += this.name + "." + this.fields[i] + "=" + record[i] + " and "
          }
        } else if ((i + 1) === this.fields.length) {
          if (!record[i]) {
            this.sql += this.name + "." + this.fields[i] + "=" + record[i] + ";"
          } else {
            this.sql += this.name + "." + this.fields[i] + "='" + record[i] + "';"
          }
        } else {
          if (!record[i]) {
            this.sql += this.name + "." + this.fields[i] + "=" + record[i] + " and "
          } else {
            this.sql += this.name + "." + this.fields[i] + "='" + record[i] + "' and "
          }

        }
      }
      console.log(this.sql)
      await axios
          .get('http://127.0.0.1:8000/delete/ ' + this.sql + '/')
          .then((response) => {
            console.log(response.data)
            this.msg = "Record successfully deleted"

          })
          .catch((error) => {
            console.log(error.response)
          })

    },
    refresh() {
      window.location.reload();
    }
  }
}
</script>

<style scoped>

</style>