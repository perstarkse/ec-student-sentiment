<template>
	<section
		data-scroll-section
		:style="topMargin ? { 'margin-top': '6rem' } : {}"
	>
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
	Filler,
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
	Filler,
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
		topMargin: {
			type: Boolean,
			default: false,
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
@import '../mixins.scss';

section {
	@include breakpoint('tablet') {
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
			@include breakpoint('tablet') {
				font-size: 3rem;
			}
			text-align: center;
			font-size: 2rem;
			font-family: 'newakeFont';
			margin-bottom: 1rem;
		}
	}
}
</style>
