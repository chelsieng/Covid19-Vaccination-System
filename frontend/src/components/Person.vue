<template>
  <p>Person works!</p>
  <button @click="test_person">CLICK HERE</button>
  <p>{{ test }}</p>
  <div class="navbar">

  <div class="subnav">
    <button class="subnavbtn">Create Data <i class="fa fa-caret-down"></i></button>
    <div class="subnav-content">
      <a href="#company">Person</a>
      <a href="#team">Public Health Facility</a>
      <a href="#careers">Public Health Worker</a>
      <a href="#company">Infection</a>
      <a href="#company">Group Age</a>
      <a href="#company">Province</a>
      <a href="#company">Vaccine</a>

    </div>
  </div> 
  <div class="subnav">
    <button class="subnavbtn">Edit Data</i></button>
   
  </div> 
  <a href="#contact">Shipment</a>
  <a href="#contact">Transfer</a>
  <a href="#contact">Queries Executor</a>
</div>

<div style="padding:0 16px">
  <h3>Edit </h3>

  <div class="dropdown">
  <button class="dropbtn">Persons</button>
  <div class="dropdown-content">
    <a href="#">Persons</a>
    <a href="#">Public Health Worker</a>
    <a href="#">Public Health Worker</a>
    <a href="#">Public Health Facility</a>
    <a href="#">Vaccination</a>
    <a href="#">infection</a>
    <a href="#">Group Age</a>
    <a href="#">Province</a>
   
  </div>
</div>
	<br/><br/><br/><br/>
    <h3>Enter the queries you want to execute<h3>
	<input type = "text"  size = "100"> </input>
    <button> execute </button>
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
body {
  font-family: Arial, Helvetica, sans-serif;
  margin: 0;
}

.navbar {
  overflow: hidden;
  background-color: #333; 
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.subnav {
  float: left;
  overflow: hidden;
}

.subnav .subnavbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .subnav:hover .subnavbtn {
  background-color: red;
}

.subnav-content {
  display: none;
  position: absolute;
  left: 0;
  background-color: red;
  width: 100%;
  z-index: 1;
}

.subnav-content a {
  float: left;
  color: white;
  text-decoration: none;
}

.subnav-content a:hover {
  background-color: #eee;
  color: black;
}

.subnav:hover .subnav-content {
  display: block;
}

.dropbtn {
  background-color: #04AA6D;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: #3e8e41;}
</style>
