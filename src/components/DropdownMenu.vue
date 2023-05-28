<template>
	<div class="dropdown-menu">
		<button class="dropdown-button" v-on:click.stop="toggleMenu">Menu</button>
		<div class="dropdown-menu-content shadow" v-if="isMenuOpen">
			<a v-for="item in menuItems" :key="item.text" :href="item.link">
				<i :class="item.icon"></i> {{ item.text }}
			</a>
		</div>
	</div>
</template>

<script>
export default {
	name: 'DropdownMenu',
	props: {
		menuItems: {
			type: Array,
			required: true,
		},
	},
	data() {
		return {
			isMenuOpen: false,
		};
	},
	methods: {
		toggleMenu() {
			this.isMenuOpen = !this.isMenuOpen;
		},
		handleClickOutside(event) {
			if (!this.$el.contains(event.target)) {
				this.isMenuOpen = false;
			}
		},
	},
	mounted() {
		document.addEventListener('click', this.handleClickOutside);
	},
	beforeUnmount() {
		document.removeEventListener('click', this.handleClickOutside);
	},
};
</script>
<style lang="scss" scoped>
.dropdown-button {
	background-color: #3b71a7;
	border-radius: 5px;
	border: 1px solid #305a85;
	color: white;
	padding: 8px 16px;
	font-size: 16px;
	cursor: pointer;
}
.dropdown-menu {
	position: relative;
}

.dropdown-menu-content {
	position: absolute;
	border-radius: 5px;
	right: 0;
	padding: 10px;
	margin-top: 15px;
	background-color: #7eb0e2;
	min-width: 160px;
	z-index: 1;
	border-radius: 5px;
	display: flex;
	gap: 10px;
	flex-direction: column;
}

.dropdown-menu-content a {
	color: black;
	text-decoration: none;
	display: block;
	font-size: 16px;
	text-align: center;
	transition: 0.2s ease-in-out;

	&:hover {
		scale: 1.1;
	}
}
</style>
