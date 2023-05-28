<template>
	<section class="vh100">
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
	</section>
</template>
<script>
export default {
	name: 'ProgressJournal',
	props: {
		initialSteps: {
			type: String,
			required: true,
		},
		dataCollection: {
			type: String,
			required: true,
		},
		dataCleaning: {
			type: String,
			required: true,
		},
		dataAnalysis: {
			type: String,
			required: true,
		},
	},
};
</script>
