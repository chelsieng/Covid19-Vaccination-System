<template>
  <div class="uk-container">
    <h2>{{ this.name }}</h2>
    <p>Total records: {{ this.results.length }}</p>
    <div class="uk-align-left "><a @click="addRow()" href="#" class="uk-icon-button uk-text-primary" uk-icon="plus"
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
        <tbody>
        <tr v-for="i in counter" :key="i">
          <td class="uk-text-center" v-for="j in fields.length" :key="j"><input :ref="'new_info' + j"
                                                                                class="uk-input uk-form-blank uk-form-width-medium"
                                                                                type="text"
                                                                                placeholder="Enter here"></td>
          <td>
            <button @click="create('new_info1')" class="uk-button uk-button-default uk-text-primary">
              Save
            </button>
          </td>
        </tr>
        <tr v-for="result in results.length" :key="result">
          <td class="uk-text-center" v-for="i in fields.length" :key="i"><input v-if="this.modify"
                                                                                class="uk-input uk-form-width-medium"
                                                                                type="text"
                                                                                placeholder="Enter here" :value="results[result-1][i-1]"><span v-else>{{ results[result-1][i-1] }}</span></td>
<!--          <td v-else class="uk-text-center" v-for="i in fields.length" :key="i"></td>-->
          <td><a @click="edit(result)" ref="edit" href="#" class="uk-icon-button uk-text-primary" uk-icon="pencil"
                 uk-tooltip="title: Edit data"></a></td>
          <td><a @click="remove(results[result-1])" ref="delete" href="#" class="uk-icon-button uk-text-danger" uk-icon="trash"
                 uk-tooltip="title: Delete record" uk-toggle="target: #modal"></a></td>
        </tr>
        </tbody>
      </table>
    </div>
    <!--    modal-->
    <div id="modal" uk-modal="bg-close: false">
      <div class="uk-modal-dialog uk-modal-body uk-text-center">
        <h3 class="uk-text-center">{{ this.msg }}</h3>
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
      counter: 0,
      modify: false
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
            // console.log(response)
            this.message = "Results: "
            this.fields = response.data["attributes"]
            this.results = response.data["results"];
          })
          .catch((error) => {
            console.log(error.response)
          })
    },
    addRow() {
      this.counter++;
    },
    async create(r) {
      console.log(r)
      console.log(this.$refs['newinfo1'])
      console.log(this.$refs['newinfo2'])

    },
    async edit(r) {
      this.modify = !this.modify
      console.log(r)
      console.log(this.$refs.edit.in)
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
            this.sql += this.name + "." + this.fields[i] + "is null;"
          } else {
            this.sql += this.name + "." + this.fields[i] + "='" + record[i] + "';"
          }
        } else {
          if (!record[i]) {
            this.sql += this.name + "." + this.fields[i] + "is null and "
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
            if (response.data) {
              this.msg = "Record successfully deleted"
            } else {
              this.msg = "Delete record unsuccessful"
            }


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