<template>
	<main ref="container">
		<WelcomeView />
		<MainOverviewChart />
		<!-- <DescriptionSection
		:purpose="purpose"
		:method="method"
		:result="result"
		:conclusion="conclusion"
	/> -->
		<ProgressJournal
			:initial-steps="initialSteps"
			:data-collection="dataCollection"
			:data-cleaning="dataCleaning"
			:data-analysis="dataAnalysis"
		/>
		<FinishedView />
	</main>
</template>

<script>
// import DropdownMenu from './components/DropdownMenu.vue';
import { textAssets } from './assets/text-assets.ts';
import MainOverviewChart from './components/MainOverviewChart.vue';
import WelcomeView from './components/WelcomeView.vue';
// import DescriptionSection from './components/DescriptionSection.vue';
import ProgressJournal from './components/ProgressJournal.vue';
import LocomotiveScroll from 'locomotive-scroll';
import FinishedView from './components/FinishedView.vue';

export default {
	name: 'App',
	components: {
		// DropdownMenu,
		MainOverviewChart,
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
		};
	},
	methods: {
		setLocomotiveScroll() {
			new LocomotiveScroll({
				el: this.$refs.container,
				smooth: true,
				multiplier: 2,
			});
		},
	},
	mounted() {
		this.setLocomotiveScroll();
	},
};
</script>

<style lang="scss">
main {
	background-image: url('@/assets/gradient2.jpg');
	background-size: cover; /* Cover the entire space of the element */
	background-position: center; /* Center the background */
	background-repeat: no-repeat; /* Do not repeat the image */
}
</style>
