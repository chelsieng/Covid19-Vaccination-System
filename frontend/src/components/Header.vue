<template>
  <nav class="uk-navbar-container uk-margin" uk-navbar="mode: click">
    <div class="uk-navbar-left">

      <ul class="uk-navbar-nav">
        <li  class="uk-active"><a href="/query">Query Executer</a></li>
        <li>
          <a href="#">Create Data</a>
          <div class="uk-navbar-dropdown">
            <ul class="uk-nav uk-navbar-dropdown-nav">
              <li class="uk-active"><a href="#">Person</a></li>
              <li><a href="#">Item</a></li>
              <li><a href="#">Item</a></li>
            </ul>
          </div>
        </li>
        <li>
          <a href="#">Edit Data</a>
          <div class="uk-navbar-dropdown">
            <ul class="uk-nav uk-navbar-dropdown-nav">
              <li class="uk-active"><a href="#">Edit Data</a></li>
              <li><a href="#">Item</a></li>
              <li><a href="#">Item</a></li>
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
  name: "Header"
}
</script>

<style scoped>

</style>