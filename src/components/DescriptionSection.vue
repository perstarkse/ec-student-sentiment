<template>
	<section class="">
		<div class="description">
			<div class="purpose">
				<h3>Purpose</h3>
				<p>{{ purpose }}</p>
			</div>
			<div class="method">
				<h3>Methodology</h3>
				<p>{{ method }}</p>
			</div>
			<div class="result">
				<h3>Result</h3>
				<p>{{ result }}</p>
			</div>
			<div class="conclusion">
				<h3>Conclusion</h3>
				<p>{{ conclusion }}</p>
			</div>
		</div>
	</section>
</template>
<script>
export default {
	name: 'DescriptionSection',
	props: {
		purpose: {
			type: String,
			required: true,
		},
		method: {
			type: String,
			required: true,
		},
		result: {
			type: String,
			required: true,
		},
		conclusion: {
			type: String,
			required: true,
		},
	},
};
</script>
