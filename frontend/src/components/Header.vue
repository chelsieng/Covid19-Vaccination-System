<template>
  <nav class="uk-navbar-container uk-margin" uk-navbar="mode: click">
    <div class="uk-navbar-left">
      <ul class="uk-navbar-nav">
        <li class="uk-active"><a href="/query">Query Executer</a></li>
        <li>
          <a href="/create">Create Data</a>
          <div class="uk-navbar-dropdown">
            <ul class="uk-nav uk-navbar-dropdown-nav">
              <li class="uk-active"><a href="#">Person</a></li>
              <li><a href="#">Item</a></li>
              <li><a href="#">Item</a></li>
            </ul>
          </div>
        </li>
        <li>
          <a href="#">Tables</a>
          <div class="uk-navbar-dropdown">
            <ul class="uk-nav uk-navbar-dropdown-nav">
              <li>
                <a :href="$router.resolve({name:'Modify', params: {table: 'Persons'}}).href">Person</a>
              </li>
              <li>
                <a :href="$router.resolve({name:'Modify', params: {table: 'Public_Health_Workers'}}).href">Public Health
                  Worker
                </a>
              </li>
              <li>
                <a :href="$router.resolve({name:'Modify', params: {table: 'Public_Health_Facilities'}}).href">Public
                  Health Facility
                </a>
              </li>
              <li><a :href="$router.resolve({name:'Modify', params: {table: 'Vaccinations'}}).href">Vaccination</a></li>
              <li><a :href="$router.resolve({name:'Modify', params: {table: 'infected'}}).href">Infection</a></li>
              <li><a :href="$router.resolve({name:'Modify', params: {table: 'Age_Groups'}}).href">Age Group</a></li>
              <li><a :href="$router.resolve({name:'Modify', params: {table: 'Provinces'}}).href">Province</a></li>
            </ul>
          </div>
        </li>
        <li><a href="#">Shipment</a></li>
        <li><a href="#">Transfer</a></li>
      </ul>

    </div>
  </nav>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      table: ""
    }
  },
  methods: {},
}
</script>

<style scoped>

</style>