<template>
  <main ref="container">
    <WelcomeView @scrollTo="scrollTo" />
    <ChartView :dataset="sentimentData" :title="'Sentiment overview'" />
    <!-- <DescriptionSection
		:purpose="purpose"
		:method="method"
		:result="result"
		:conclusion="conclusion"
	/> -->
    <ChartView
      :dataset="stressData"
      :title="'Additional variables'"
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
// import DropdownMenu from './components/DropdownMenu.vue';
import { textAssets } from "./assets/text-assets.ts";
import ChartView from "./components/ChartView.vue";
import WelcomeView from "./components/WelcomeView.vue";
// import DescriptionSection from './components/DescriptionSection.vue';
import ProgressJournal from "./components/ProgressJournal.vue";
import LocomotiveScroll from "locomotive-scroll";
import FinishedView from "./components/FinishedView.vue";
import { sentimentData, stressData } from "@/assets/datasets.ts";

export default {
  name: "App",
  components: {
    // DropdownMenu,
    ChartView,
    WelcomeView,
    // DescriptionSection,
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
  },
};
</script>

<style lang="scss">
@font-face {
  font-family: "newakeFont";
  src: url("~@/assets/fonts/Newake-Font-Demo.otf") format("opentype");
}
main {
  background-image: url("@/assets/gradient2.jpg");
  background-size: cover; /* Cover the entire space of the element */
  background-position: center; /* Center the background */
  background-repeat: no-repeat; /* Do not repeat the image */
}
</style>
