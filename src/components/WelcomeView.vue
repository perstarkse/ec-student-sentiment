<template>
	<main>
		<section data-scroll data-scroll-speed="1.5" data-scroll-section>
			<div class="container">
				<div class="title-holder" data-scroll-speed="0.5" data-scroll>
					<h1>Student Sentiment</h1>
					<h3>Student sentiment for the fullstack developer course.</h3>
				</div>
				<div class="img-holder">
					<img
						data-scroll
						data-scroll-speed="2"
						src="../assets/undraw-chart.svg"
						alt="chart"
					/>
				</div>
				<div class="image-holder" style="display: none">
					<img
						data-scroll
						data-scroll-speed="4"
						class="first"
						src="../assets/heart-eyes.png"
					/>
					<img
						data-scroll
						data-scroll-speed="2"
						class="second"
						src="../assets/frustrated.png"
					/>
					<img
						data-scroll
						data-scroll-speed="6"
						class="third"
						src="../assets/smiling.png"
					/>
					<img
						data-scroll
						data-scroll-speed="3"
						class="fourth"
						src="../assets/yawn.png"
					/>
					<img
						data-scroll
						data-scroll-speed="10"
						class="fifth"
						src="../assets/stars.png"
					/>
				</div>
				<div style="text-align: center">
					<svg
						class="scroll-down"
						xmlns="http://www.w3.org/2000/svg"
						height="1em"
						viewBox="0 0 512 512"
					>
						<!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
						<path
							d="M233.4 406.6c12.5 12.5 32.8 12.5 45.3 0l192-192c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L256 338.7 86.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l192 192z"
						/>
					</svg>
				</div>
			</div>
		</section>
	</main>
</template>

<script>
import undrawChart from '@/assets/undraw-chart.svg';

export default {
	name: 'WelcomeView',
	methods: {},
	components: {},
	data() {
		return {
			undrawChart,
		};
	},
};
</script>

<style lang="scss" scoped>
@import '../mixins.scss';

section {
	/* background-color: #2a9d8f; */
	display: flex;
	justify-content: center;
	align-items: center;
}
.container {
	display: grid;
	height: 100vh;
	place-items: center;
	position: relative;
	max-width: 1920px;
	.title-holder {
		@include breakpoint('desktop') {
			margin-right: 10rem;
			margin-left: 2rem;
		}
		@include breakpoint('xlarge') {
			margin-right: 30rem;
			margin-left: 2rem;
		}
		margin-left: 1rem;
		z-index: 100;
		h1 {
			@include breakpoint('desktop') {
				font-size: 10rem;
			}
			@include breakpoint('tablet') {
				font-size: 7rem;
			}
			cursor: default;
			font-size: 4.5rem;
			color: #940094;
			font-family: 'newakeFont';
			/* text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25); */
			width: 100%;
			z-index: 100;
		}
		h3 {
			@include breakpoint('desktop') {
				width: 70%;
				font-size: 2.5rem;
			}
			@include breakpoint('tablet') {
				font-size: 2rem;
			}
			cursor: default;
			font-size: 1.5rem;
			color: #000000;
			font-family: 'newakeFont';
			width: 90%;
			z-index: 10;
		}
	}
	.img-holder {
		@include breakpoint('desktop') {
			position: absolute;
			display: block;
			top: 50%;
			right: 2%;
		}
		display: none;
	}

	.first {
		position: absolute;
		bottom: 20%;
		right: 10%;
		z-index: 1;

		height: 120px;
		@include breakpoint('mobile') {
			height: 200px;
		}
		@include breakpoint('desktop') {
			height: 350px;
		}
	}
	.second {
		position: absolute;
		bottom: 60%;
		right: 5%;
		z-index: 2;
		height: 120px;
		@include breakpoint('mobile') {
			height: 200px;
		}
		@include breakpoint('desktop') {
			height: 350px;
		}
	}
	.third {
		position: absolute;
		bottom: 14%;
		right: 5%;
		z-index: 3;
		height: 120px;
		@include breakpoint('mobile') {
			height: 200px;
		}
		@include breakpoint('desktop') {
			height: 350px;
		}
	}
	.fourth {
		position: absolute;
		bottom: 60%;
		right: 20%;
		z-index: 4;
		height: 120px;
		@include breakpoint('mobile') {
			height: 200px;
		}
		@include breakpoint('desktop') {
			height: 350px;
		}
	}
	.fifth {
		position: absolute;
		bottom: 30%;
		right: 30%;
		z-index: 5;
		height: 120px;
		@include breakpoint('mobile') {
			height: 200px;
		}
		@include breakpoint('desktop') {
			height: 350px;
		}
	}
	.scroll-down {
		position: absolute;
		bottom: 5%;
		left: 47%;
		font-size: 50px;
		transform-origin: center;
		animation: pulse 2s infinite;
		animation-delay: 3s;
		fill: white;
		display: none;
	}
}
@keyframes pulse {
	0% {
		transform: scale(1);
	}
	50% {
		transform: scale(1.3);
	}
	100% {
		transform: scale(1);
	}
}
</style>
