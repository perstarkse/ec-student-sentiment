<template>
	<div class="topbar shadow">
		<h2>EC STUDENT SENTIMENT</h2>
		<div class="dropdown">
			<DropdownMenu :menu-items="socials" />
		</div>
	</div>
	<div class="vh100" style="display: none">
		<div class="introduction">
			<p class="breadtext shadow">{{ introduction }}</p>
		</div>
	</div>
	<div class="" style="display: block; padding-top: 5rem">
		<div class="">
			<MainOverviewChart />
		</div>
	</div>
	<div class="vh100">
		<div class="description">
			<div class="purpose breadtext shadow">
				<h3>Purpose</h3>
				<p>{{ purpose }}</p>
			</div>
			<div class="method breadtext shadow">
				<h3>Methodology</h3>
				<p>{{ method }}</p>
			</div>
			<div class="result breadtext shadow">
				<h3>Result</h3>
				<p>{{ result }}</p>
			</div>
			<div class="conclusion breadtext shadow">
				<h3>Conclusion</h3>
				<p>{{ conclusion }}</p>
			</div>
		</div>
	</div>
	<div class="vh100">
		<div class="progress-journal">
			<h2>Progress Journal</h2>
			<div class="initialSteps breadtext shadow">
				<h3>Initial Steps</h3>
				<p>{{ initialSteps }}</p>
			</div>
			<div class="dataCollection breadtext shadow">
				<h3>Data Collection</h3>
				<p>{{ dataCollection }}</p>
			</div>
			<div class="dataCleaning breadtext shadow">
				<h3>Data Cleaning</h3>
				<p>{{ dataCleaning }}</p>
			</div>
			<div class="dataAnalysis breadtext shadow">
				<h3>Data Analysis</h3>
				<p>{{ dataAnalysis }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import DropdownMenu from './components/DropdownMenu.vue';
import { textAssets } from './assets/text-assets.ts';
import MainOverviewChart from './components/MainOverviewChart.vue';

export default {
	name: 'App',
	components: {
		DropdownMenu,
		MainOverviewChart,
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
