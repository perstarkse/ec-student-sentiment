<template>
	<!-- <header class="topbar shadow">
		<h2>EC STUDENT SENTIMENT</h2>
		<div class="dropdown">
			<DropdownMenu :menu-items="socials" />
		</div>
	</header> -->
	<!-- <WelcomeView :introduction="introduction" /> -->
	<section class="" style="display: block; padding-top: 5rem">
		<div class="">
			<MainOverviewChart />
		</div>
	</section>
	<!-- <DescriptionSection
		:purpose="purpose"
		:method="method"
		:result="result"
		:conclusion="conclusion"
	/>
	<ProgressJournal
		:initial-steps="initialSteps"
		:data-collection="dataCollection"
		:data-cleaning="dataCleaning"
		:data-analysis="dataAnalysis"
	/> -->
</template>

<script>
// import DropdownMenu from './components/DropdownMenu.vue';
import { textAssets } from './assets/text-assets.ts';
import MainOverviewChart from './components/MainOverviewChart.vue';
// import WelcomeView from './components/WelcomeView.vue';
// import DescriptionSection from './components/DescriptionSection.vue';
// import ProgressJournal from './components/ProgressJournal.vue';
import LocomotiveScroll from 'locomotive-scroll';

export default {
	name: 'App',
	components: {
		// DropdownMenu,
		MainOverviewChart,
		// WelcomeView,
		// DescriptionSection,
		// ProgressJournal,
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
			this.scroll = new LocomotiveScroll({
				el: document.querySelector('[data-scroll-container]'),
				smooth: true,
				direction: 'horizontal',
			});
		},
	},
	// mounted() {
	// 	this.setLocomotiveScroll();
	// },
};
</script>

<style lang="scss">
.vh100 {
	min-height: 100vh;
	display: flex;
	align-items: center;
	justify-content: center;
}
.shadow {
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.topbar {
	position: fixed;
	z-index: 100;
	width: 90%;
	height: 60px;
	background-color: #7eb0e2;
	opacity: 1;
	font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
		Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	color: black;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 24px;
	border-radius: 5px;
	margin: 0 auto;
	left: 0;
	right: 0;
}
.introduction {
	display: flex;
	justify-content: center;
}
.breadtext {
	max-width: 70%;
	text-align: center;
	font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
		Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	align-items: center;
	padding: 60px;
	background-color: #7eb0e2;
	border-radius: 5px;
}

.chart {
	width: 80%;
	height: 500px;
	background-color: #7eb0e2;
	opacity: 0.8;
	font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
		Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	color: black;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 24px;
	border-radius: 5px;
}
.dropdown {
	position: absolute;
	right: 30px;
}
.description {
	display: grid;
	place-items: center;
	gap: 2rem;
}
.progress-journal {
	h2 {
		text-align: center;
	}
	display: grid;
	place-items: center;
	gap: 2rem;
}
</style>
