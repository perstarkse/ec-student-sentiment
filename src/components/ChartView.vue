<template>
	<section data-scroll-section>
		<div id="main-chart" class="container">
			<h1>{{ title }}</h1>
			<Line :options="chartOptions" :data="dataset" />
		</div>
	</section>
</template>

<script>
import {
	Chart as ChartJS,
	CategoryScale,
	LinearScale,
	PointElement,
	LineElement,
	Title,
	Tooltip,
	Legend,
} from 'chart.js';
import { Line } from 'vue-chartjs';

ChartJS.register(
	CategoryScale,
	LinearScale,
	PointElement,
	LineElement,
	Title,
	Tooltip,
	Legend,
);
export default {
	name: 'LineChart',
	components: { Line },
	props: {
		dataset: {
			type: Object,
			required: true,
		},
		title: {
			type: String,
			required: true,
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
section {
	margin-top: 12rem;
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
			text-align: center;
			font-size: 3rem;
			font-family: 'newakeFont';
			margin-bottom: 1rem;
		}
	}
}
</style>
