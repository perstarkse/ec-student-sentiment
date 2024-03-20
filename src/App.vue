<template>
  <main ref="container">
    <WelcomeView @scrollTo="scrollTo" />
    <ChartView
      :dataset="sentimentData"
      :title="'Sentiment overview'"
      :description="'The chart measures sentiment on a scale from 0 to 100, where 100 represents a completely positive or favorable mood, and 0 indicates a very negative or unfavorable mood'"
    />
    <ChartView
      :dataset="stressData"
      :title="'Additional variables'"
      :description="'The chart measures expressed degrees of control, experienced demands, support as well as the general sentiments of the students. By pressing the buttons below you can toggle that variable.'"
      :top-margin="true"
    />
    <BarChart
      v-if="correlationData"
      :dataset="correlationData"
      :title="'Statistical Analysis'"
      :description="`This chart displays the
    Pearson's r correlation coefficients between the Demand-Control-Support
    model variables and sentiment scores. The correlation coefficient ranges
    from -1 to 1, where a value of 1 indicates a perfect positive correlation,
    -1 indicates a perfect negative correlation, and 0 indicates no correlation.`"
      :top-margin="true"
    />
    <ProgressJournal
      :data-collection="dataCollection"
      :data-cleaning="dataCleaning"
      :data-analysis="dataAnalysis"
      :data-visualization="dataVisualization"
    />
    <FinishedView :socials="socials" />
  </main>
</template>

<script>
import { textAssets } from "./assets/text-assets.ts";
import ChartView from "./components/ChartView.vue";
import WelcomeView from "./components/WelcomeView.vue";
import ProgressJournal from "./components/ProgressJournal.vue";
import LocomotiveScroll from "locomotive-scroll";
import FinishedView from "./components/FinishedView.vue";
import {
  sentimentData,
  stressData,
  correlationData,
} from "@/assets/datasets.ts";
import BarChart from "./components/BarChart.vue";

export default {
  name: "App",
  components: {
    ChartView,
    WelcomeView,
    ProgressJournal,
    FinishedView,
    BarChart,
  },
  data() {
    return {
      introduction: textAssets.introduction,
      socials: textAssets.socials,
      method: textAssets.method,
      purpose: textAssets.purpose,
      result: textAssets.result,
      conclusion: textAssets.conclusion,
      initialSteps: textAssets.initialSteps,
      dataCollection: textAssets.dataCollection,
      dataCleaning: textAssets.dataParsingAndCleaning,
      dataVisualization: textAssets.dataVisualization,
      dataAnalysis: textAssets.dataAnalysis,
      scroll: null,
      sentimentData: sentimentData,
      stressData: stressData,
      correlationData: correlationData,
    };
  },
  methods: {
    setLocomotiveScroll() {
      this.scroll = new LocomotiveScroll({
        el: this.$refs.container,
        smooth: true,
        multiplier: 2,
      });
    },
    scrollTo(selector) {
      this.scroll.scrollTo(selector, {
        duration: 1000,
        easing: [0.25, 0.46, 0.45, 0.94],
        offset: -300,
      });
    },
  },
  mounted() {
    this.setLocomotiveScroll();

    // calculate the amount of total messages in stressdata
    // let totalMessages = 0;
    // for (const course of sentimentData.datasets) {
    //   for (const week of course.data) {
    //     totalMessages += week.num_messages;
    //   }
    // }
    // console.log(totalMessages);
    // Extract the data points for each variable
    // const controlData = stressData.datasets.find(
    //   (dataset) => dataset.label === "control"
    // ).data;
    // const demandData = stressData.datasets.find(
    //   (dataset) => dataset.label === "demand"
    // ).data;
    // const supportData = stressData.datasets.find(
    //   (dataset) => dataset.label === "support"
    // ).data;
    // const sentimentData = stressData.datasets.find(
    //   (dataset) => dataset.label === "sentiment"
    // ).data;

    // // Function to calculate the Pearson correlation coefficient
    // function calculateCorrelation(x, y) {
    //   const n = x.length;
    //   const sumX = x.reduce((sum, value) => sum + value, 0);
    //   const sumY = y.reduce((sum, value) => sum + value, 0);
    //   const sumXY = x.reduce((sum, value, index) => sum + value * y[index], 0);
    //   const sumX2 = x.reduce((sum, value) => sum + value ** 2, 0);
    //   const sumY2 = y.reduce((sum, value) => sum + value ** 2, 0);

    //   const numerator = n * sumXY - sumX * sumY;
    //   const denominator = Math.sqrt(
    //     (n * sumX2 - sumX ** 2) * (n * sumY2 - sumY ** 2)
    //   );

    //   return numerator / denominator;
    // }

    // // Calculate the correlation coefficients
    // const controlSentimentCorrelation = calculateCorrelation(
    //   controlData.map((d) => d.y),
    //   sentimentData.map((d) => d.y)
    // );
    // const demandSentimentCorrelation = calculateCorrelation(
    //   demandData.map((d) => d.y),
    //   sentimentData.map((d) => d.y)
    // );
    // const supportSentimentCorrelation = calculateCorrelation(
    //   supportData.map((d) => d.y),
    //   sentimentData.map((d) => d.y)
    // );

    // this.correlationData = {
    //   labels: ["Control", "Demand", "Support"],
    //   datasets: [
    //     {
    //       label: "Correlation Coefficients",
    //       data: [
    //         0.47675679638590235, -0.26765497897453805, 0.24678697464239036,
    //       ],
    //       backgroundColor: [
    //         "rgba(255, 99, 132, 0.2)",
    //         "rgba(54, 162, 235, 0.2)",
    //         "rgba(255, 206, 86, 0.2)",
    //       ],
    //       borderColor: [
    //         "rgba(255, 99, 132, 1)",
    //         "rgba(54, 162, 235, 1)",
    //         "rgba(255, 206, 86, 1)",
    //       ],
    //       borderWidth: 1,
    //     },
    //   ],
    // };

    // // Display the results
    // console.log("Control-Sentiment Correlation:", controlSentimentCorrelation);
    // console.log("Demand-Sentiment Correlation:", demandSentimentCorrelation);
    // console.log("Support-Sentiment Correlation:", supportSentimentCorrelation);

    // // Calculate the weighted sum of control, demand, and support
    // const weightedSum = controlData.map((d, i) => {
    //   const controlValue = d.y * controlSentimentCorrelation;
    //   const demandValue = demandData[i].y * demandSentimentCorrelation;
    //   const supportValue = supportData[i].y * supportSentimentCorrelation;
    //   return controlValue - demandValue + supportValue;
    // });

    // // Calculate the correlation between the weighted sum and the actual sentiment
    // const correlationCoefficient = calculateCorrelation(
    //   weightedSum,
    //   sentimentData.map((d) => d.y)
    // );

    // // Display the results
    // console.log(
    //   "Correlation between Weighted Sum and Actual Sentiment:",
    //   correlationCoefficient
    // );
  },
};
</script>

<style lang="scss">
@font-face {
  font-family: "newakeFont";
  src: url("~@/assets/fonts/Newake-Font-Demo.otf") format("opentype");
}
main {
  background-image: url("@/assets/optiwebp.webp");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>
