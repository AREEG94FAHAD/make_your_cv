<template>
  <div id="app" class="back">
    <!-- Just an image -->
<nav class="navbar navbar-light" style="background-color: #E59866 ">
  <div class="navbar-brand" style="color: #F8F9F9">Make your CV "AREEG FAHAD"</div>
</nav>
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  // background-color: #242727;
}



#nav {
  padding: 30px;
  background-color: #717D7E;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
// html{
//   background-color: #F8F9F9;
//   width: 100%;
//   height: 100%;
// }
body{
  background: url(./back.jpg) no-repeat center center fixed; 
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  // height: 800px;
  }
</style>


