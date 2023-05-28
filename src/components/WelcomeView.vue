<template>
	<div class="vh100" style="">
		<div class="introduction">
			<p class="breadtext shadow">{{ introduction }}</p>
		</div>
	</div>
</template>
<script>
export default {
	name: 'WelcomeView',
	props: {
		introduction: {
			type: String,
			required: true,
		},
	},
};
</script>
