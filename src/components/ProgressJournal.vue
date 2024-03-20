<template>
  <section data-scroll-section>
    <div class="container" id="sticky">
      <h2>Progress Journal</h2>
      <img
        data-scroll
        data-scroll-sticky
        data-scroll-target="#sticky"
        src="../assets/analytics.png"
      />
      <br />
      <div class="dataCollection">
        <h3>Data Collection</h3>
        <p>{{ dataCollection }}</p>
      </div>
      <div class="dataCleaning">
        <h3>Data Cleaning</h3>
        <p>{{ dataCleaning }}</p>
      </div>
      <div class="dataAnalysis">
        <h3>Data Analysis</h3>
        <p>{{ dataAnalysis }}</p>
      </div>
      <div class="dataVisualization">
        <h3>Data Visualization</h3>
        <p>{{ dataVisualization }}</p>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "ProgressJournal",
  props: {
    dataCollection: {
      type: String,
      required: true,
    },
    dataCleaning: {
      type: String,
      required: true,
    },
    dataAnalysis: {
      type: String,
      required: true,
    },
    dataVisualization: {
      type: String,
      required: true,
    },
  },
};
</script>
<style lang="scss" scoped>
@import "../mixins.scss";
section {
  /* background-color: #e9c46a; */
  padding-top: 8rem;
  padding-bottom: 8rem;
  display: grid;
  place-items: center;
  .container {
    position: relative;
    max-width: 1920px;
    padding-left: 2rem;
    padding-right: 2rem;
    @include breakpoint("desktop") {
      padding-left: 5rem;
      padding-right: 5rem;
    }
    div {
      @include breakpoint("desktop") {
        padding-right: 20rem;
      }
      padding-right: 0rem;
    }
    img {
      @include breakpoint("desktop") {
        display: block;
      }
      display: none;
      position: absolute;
      top: 100px;
      right: 50px;
      height: 250px;
    }
    p {
      font-family: "sans-serif";
    }
    h2 {
      text-align: center;
      font-family: "newakeFont";
      font-size: 3rem;
      margin-bottom: 1rem;
      @include breakpoint("desktop") {
        font-size: 5rem;
      }
    }
    h3 {
      margin-bottom: 0.6rem;
      margin-top: 1.5rem;
      font-family: "newakeFont";
    }
  }
}
</style>
