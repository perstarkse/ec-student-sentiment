<template>
	<section data-scroll-section>
		<div class="container">
			<h1>Finished</h1>
			<p>
				Thank you for taking the time to look at my project. I hope you enjoyed
				it. If you have any questions or feedback, please feel free to contact
				me.
			</p>
			<div class="socials">
				<a href="https://www.linkedin.com/in/alexander-lee-1b1b3b1b0/">
					<!-- <img src="../assets/linkedin.svg" alt="linkedin" /> -->
				</a>
			</div>
		</div>
	</section>
</template>
<script>
export default {
	name: 'FinishedView',
};
</script>
<style lang="scss" scoped>
section {
	padding-bottom: 20rem;
	display: grid;
	place-items: center;
	.container {
		background-color: #f5ebe0;
		padding-top: 10rem;
		padding-bottom: 20rem;
		width: 100%;
		position: relative;
		max-width: 1920px;
		padding-left: 5rem;
		padding-right: 5rem;
		text-align: center;

		img {
			position: absolute;
			top: 50px;
			right: -50px;
			height: 250px;
		}
		h1 {
			font-family: 'newakeFont';
			font-size: 3rem;
			margin-bottom: 2rem;
		}
		p {
			margin-bottom: 2rem;
			font-family: 'sans-serif';
		}
	}
}
</style>
