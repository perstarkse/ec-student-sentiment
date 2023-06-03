<template>
	<section data-scroll-section>
		<div class="container">
			<h1>Sentiment overview</h1>
			<Line :options="chartOptions" :data="chartData" />
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
	data() {
		return {
			chartData: {
				labels: [
					'08-25-2022-1',
					'08-25-2022-2',
					'08-26-2022',
					'08-27-2022',
					'08-28-2022',
					'08-29-2022',
					'08-30-2022',
					'08-31-2022',
					'09-01-2022',
					'09-02-2022',
					'09-03-2022',
					'09-04-2022',
					'09-05-2022',
					'09-06-2022',
					'09-07-2022',
					'09-08-2022-1',
					'09-08-2022-2',
					'09-09-2022',
					'09-10-2022',
					'09-11-2022',
					'09-12-2022',
					'09-13-2022',
					'09-14-2022-1',
					'09-14-2022-2',
					'09-15-2022',
					'09-16-2022',
					'09-17-2022',
					'09-18-2022',
					'09-19-2022',
					'09-20-2022',
					'09-21-2022',
					'09-22-2022',
				],
				datasets: [
					{
						label: 'Frustration level',
						data: [
							60, 20, 30, 50, 70, 70, 60, 30, 0, 60, 20, 70, 60, 20, 30, 20, 30,
							20, 20, 0, 30, 60, 50, 20, 20, 50, 60, 60, 30, 60, 30, 80, 30, 60,
							40, 70,
						],
						fill: false,
						borderColor: 'rgb(75, 192, 192)',
						tension: 0.5,
					},
					{
						label: 'Happiness level',
						data: [
							40, 60, 70, 30, 30, 30, 40, 70, 70, 40, 60, 30, 40, 60, 50, 60,
							70, 60, 60, 70, 70, 40, 40, 70, 80, 70, 40, 40, 70, 40, 50, 20,
							50, 40, 60, 30,
						],
						fill: false,
						borderColor: 'rgb(255, 99, 132)',
						tension: 0.5,
					},
				],
			},
			chartOptions: {
				responsive: true,
			},
		};
	},
};
</script>
<style lang="scss" scoped>
section {
	padding-top: 9rem;
	padding-bottom: 9rem;
	display: grid;
	place-items: center;
	background-color: #f5ebe0;
	.container {
		width: 90%;
		display: flex;
		flex-direction: column;
		align-items: center;
		max-width: 1920px;
	}
}
h1 {
	text-align: center;
}
</style>
