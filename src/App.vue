<template>
	<div class="topbar shadow">
		<h2>EC STUDENT SENTIMENT</h2>
		<div class="dropdown"><DropdownMenu :menu-items="socials" /></div>
	</div>
	<div class="vh100">
		<div class="introduction">
			<p class="breadtext shadow">{{ introduction }}</p>
		</div>
	</div>
	<div class="vh100">
		<div class="chart">TEMPLATE CHART</div>
	</div>
	<div class="vh100">
		<div class="description">
			<p class="purpose shadow">{{ purpose }}</p>
			<p class="method shadow">{{ method }}</p>
			<p class="result shadow">{{ result }}</p>
			<p class="conclusion shadow">{{ conclusion }}</p>
		</div>
	</div>
</template>

<script>
import DropdownMenu from './components/DropdownMenu.vue';

export default {
	name: 'App',
	components: {
		DropdownMenu,
	},
	data() {
		return {
			introduction:
				'The project, titled "Webbutvecklare Distans Gänget - Sentiment Tracker,"...',
			socials: [
				{ icon: 'twitter', text: 'Twitter', link: 'https://twitter.com' },
				{ icon: 'web', text: 'Webpage', link: 'https://website.com' },
				{ icon: 'linkedin', text: 'LinkedIn', link: 'https://linkedin.com' },
			],
		};
	},
};
</script>

<style lang="scss">
.vh100 {
	height: 100vh;
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
</style>
