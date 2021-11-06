<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <div>
    <Header />
    <Main />
    <Footer />
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import Main from "./components/MainContent.vue";
import Header from "./components/TheHeader.vue";
import Footer from "./components/TheFooter.vue";

export default {
  name: "App",
  components: {
    Header,
    Main,
    Footer,
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma/bulma.sass";
@import url('https://fonts.googleapis.com/css2?family=Rampart+One&display=swap');
</style>
