<template>
  <p>Person works!</p>
  <button @click="test_person">CLICK HERE</button>
  <p>{{ test }}</p>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      error: '',
      test: ""
    }
  },
  methods: {
    async test_person() {
      await axios
          .get('http://127.0.0.1:8000/function/')
          .then((response) => {
            console.log(response)
            this.test = response.data;
          })
          .catch((error) => {
            console.log(error.response)
          })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
