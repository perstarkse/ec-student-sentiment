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
      :description="'The chart measures expressed degrees of control, experienced demands, support as well as the general semtiments of the students. By pressing the buttons below you can toggle that variable.'"
      :top-margin="true"
    />
    <ProgressJournal
      :initial-steps="initialSteps"
      :data-collection="dataCollection"
      :data-cleaning="dataCleaning"
      :data-analysis="dataAnalysis"
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
import { sentimentData, stressData } from "@/assets/datasets.ts";

export default {
  name: "App",
  components: {
    ChartView,
    WelcomeView,
    ProgressJournal,
    FinishedView,
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
      dataCleaning: textAssets.dataCleaning,
      dataAnalysis: textAssets.dataAnalysis,
      scroll: null,
      sentimentData: sentimentData,
      stressData: stressData,
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
