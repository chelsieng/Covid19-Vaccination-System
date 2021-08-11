<template>
  <div class="uk-container">
    <p class="uk-text-left uk-legend">Personal information:</p>
    <form class="uk-grid-small" uk-grid>
      <div class="uk-width-1-2@s uk-text-left">
        <label>First Name</label>
        <input class="uk-input" type="text" placeholder="Enter first name">
      </div>
      <div class="uk-width-1-2@s uk-text-left">
        <label>Last Name</label>
        <input class="uk-input" type="text" placeholder="Enter last name">
      </div>
      <div class="uk-width-1-3@s uk-text-left">
        <label>Date of Birth</label>
        <input class="uk-input" type="text" placeholder="YYYY-MM-DD">
      </div>
      <div class="uk-width-1-3@s uk-text-left">
        <label>Telephone Number</label>
        <input class="uk-input" type="text" placeholder="Enter phone number">
      </div>
      <div class="uk-width-1-3@s uk-text-left">
        <label>Email</label>
        <input class="uk-input" type="text" placeholder="abc@example.com">
      </div>
      <div class="uk-width-1-4@s uk-text-left">
        <label>Address</label>
        <input class="uk-input" type="text" placeholder="Civic no., Street Name">
      </div>
      <div class="uk-width-1-4@s uk-text-left">
        <label>City</label>
        <input class="uk-input" type="text" placeholder="City">
      </div>
      <div class="uk-width-1-4@s uk-text-left">
        <label>Province</label>
        <input class="uk-input" type="text" placeholder="Province">
      </div>
      <div class="uk-width-1-4@s uk-text-left">
        <label>Postal Code</label>
        <input class="uk-input" type="text" placeholder="Postal Code">
      </div>
       <div class="uk-width-1-3@s uk-text-left">
         <label>Citizenship</label>
        <div>
            <label><input class="uk-radio" type="radio" name="radio1"> Canadian</label><br>
            <label><input class="uk-radio" type="radio" name="radio1"> Other:</label> <input class="uk-input uk-form-blank uk-form-width-medium" type="text" placeholder="Enter citizenship">
        </div>
      </div>
      <div class="uk-width-1-3@s uk-text-left">
        <label>Social Security Number</label>
        <input class="uk-input" type="text" placeholder="SSN">
      </div>
      <div class="uk-width-1-3@s uk-text-left">
        <label>Passport Number</label>
        <input class="uk-input" type="text" placeholder="Passport Number">
      </div>
      <p class="uk-text-left uk-legend">Infection:</p>
      <div class="uk-width-1-1@s uk-text-left">
         <label>Have you ever been infected by COVID-19?</label>
        <div>
            <label><input class="uk-radio" type="radio" name="radio1"> Yes: </label> <input class="uk-input uk-form-blank uk-form-width-medium" type="text" placeholder="Enter date of infection"> <input class="uk-input uk-form-blank uk-form-width-medium" type="text" placeholder="Enter type of infection"><br>
            <label><input class="uk-radio" type="radio" name="radio1"> No</label>
        </div>
      </div>
      <p class="uk-text-left uk-legend">Employment:</p>
       <div class="uk-width-1-1@s uk-text-left">
         <label>Are you a public health worker?</label>
        <div>
            <label><input class="uk-radio" type="radio" name="radio1"> Yes: </label> <input class="uk-input uk-form-blank uk-form-width-medium" type="text" placeholder="Enter Employee ID"> If applicable: <input class="uk-input uk-form-blank uk-form-width-medium" type="text" placeholder="Enter Manager ID"> <input class="uk-input uk-form-blank uk-form-width-medium" type="text" placeholder="Enter Health Facility"><br>
            <label><input class="uk-radio" type="radio" name="radio1"> No</label>
        </div>
      </div>
    </form>
  </div>


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
