<template>
  <section
    data-scroll-section
    :style="topMargin ? { 'margin-top': '6rem' } : {}"
  >
    <div id="main-chart" class="container">
      <h1>{{ title }}</h1>
      <p v-if="description.length" class="description">{{ description }}</p>
      <Bar :options="chartOptions" :data="dataset" />
    </div>
  </section>
</template>

<script>
import {
  Chart as ChartJS,
  Title,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  BarElement,
} from "chart.js";
import { Bar } from "vue-chartjs";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: { Bar },
  props: {
    dataset: {
      type: Object,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    topMargin: {
      type: Boolean,
      default: false,
    },
    description: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
      },
    };
  },
};
</script>
<style lang="scss" scoped>
@import "../mixins.scss";

section {
  @include breakpoint("tablet") {
    margin-top: 12rem;
  }
  padding-top: 4rem;
  padding-bottom: 6rem;
  display: grid;
  place-items: center;
  background-color: #f5ebe0;
  .container {
    width: 90%;
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 1920px;
    h1 {
      @include breakpoint("tablet") {
        font-size: 3rem;
      }
      text-align: center;
      font-size: 2rem;
      font-family: "newakeFont";
      margin-bottom: 1rem;
    }
  }
}
.description {
  text-align: center;
  margin-bottom: 1rem;
  font-size: 0.9em;
  color: #6c6c6c;
}
</style>
