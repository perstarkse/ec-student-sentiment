<template>
  <main>
    <section data-scroll data-scroll-speed="1.5" data-scroll-section>
      <div class="container">
        <div class="title-holder" data-scroll-speed="0.5" data-scroll>
          <h1>Student Sentiment</h1>
          <h3>
            Psychological analysis regarding the fullstack developer course.
          </h3>
          <button @click="scrolldown">See the charts</button>
        </div>
        <div class="img-holder">
          <img
            data-scroll
            data-scroll-speed="2"
            src="../assets/undraw-chart.svg"
            alt="chart"
          />
        </div>
      </div>
    </section>
  </main>
</template>
<script>
import undrawChart from "@/assets/undraw-chart.svg";

export default {
  name: "WelcomeView",
  methods: {
    scrolldown() {
      this.$emit("scrollTo", "#main-chart");
    },
  },
  components: {},
  data() {
    return {
      undrawChart,
    };
  },
};
</script>
<style lang="scss" scoped>
@import "../mixins.scss";

section {
  display: flex;
  justify-content: center;
  align-items: center;
}
.container {
  display: flex;
  height: 100vh;
  position: relative;
  max-width: 1920px;
  .title-holder {
    @include breakpoint("desktop") {
      margin-right: 10rem;
      margin-left: 2rem;
      margin-top: 10vh;
    }
    @include breakpoint("xlarge") {
      margin-right: 30rem;
      margin-top: 15vh;
      margin-left: 2rem;
    }
    margin-left: 1rem;
    z-index: 100;
    margin-top: 25vh;
    h1 {
      @include breakpoint("tablet") {
        font-size: 8rem;
      }
      @include breakpoint("desktop") {
        font-size: 10rem;
      }
      @include breakpoint("xlarge") {
        font-size: 12rem;
      }
      cursor: default;
      font-size: 4.5rem;
      color: #940094;
      font-family: "newakeFont";
      /* text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25); */
      width: 100%;
      z-index: 100;
    }
    button {
      background-color: #ff00ff48;
      border: none;
      border-radius: 5px;
      padding: 4px 12px;
      margin-top: 1rem;
      color: black;
      cursor: pointer;
      transition: 0.3s ease-in-out;
      &:hover {
        background-color: #882d88;
      }
    }
    h3 {
      @include breakpoint("tablet") {
        font-size: 2rem;
      }
      @include breakpoint("desktop") {
        width: 70%;
        font-size: 2.5rem;
      }

      cursor: default;
      font-size: 1.5rem;
      color: #000000;
      font-family: "newakeFont";
      width: 90%;
      z-index: 10;
    }
  }
  .img-holder {
    @include breakpoint("desktop") {
      position: absolute;
      display: block;
      top: 50%;
      right: 2%;
    }
    display: none;
  }

  .scroll-down {
    position: absolute;
    bottom: 5%;
    left: 47%;
    font-size: 50px;
    transform-origin: center;
    animation: pulse 2s infinite;
    animation-delay: 3s;
    fill: white;
    display: none;
  }
}
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.3);
  }
  100% {
    transform: scale(1);
  }
}
</style>
