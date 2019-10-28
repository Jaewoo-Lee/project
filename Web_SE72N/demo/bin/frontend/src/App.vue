<template>
	<!-- <v-app v-resize-text> -->
	<v-app id="top_page">

		<v-content>
			<router-view/>
		</v-content>

		<v-btn
			color="rgba(0, 0, 0, 0.5)"
			v-show="scrolled"
			@click="$vuetify.goTo('#top_page')"
			style="z-index:5;"
			dark fab bottom right fixed>
			<v-icon large>keyboard_arrow_up</v-icon>
		</v-btn>

	</v-app>
</template>

<script>
import 'es6-promise/auto'
import store from '@/store'
import controller from '@/services/Controller'
import FirebaseService from '@/services/FirebaseService'

export default {
	name: 'App',
	data() {
		return {
			scrolled: false
		};
	},
	store,
	components: {
	},
	methods: {
		handleScroll() {
			this.scrolled = window.scrollY > 0;
		},
		async getPortfolios() {
			await controller.getPortfolios();
		},
		async getPosts() {
			await controller.getPosts();
		},
		async pushMessaging(){
			await FirebaseService.pushMessaging();
		}
	},
	created() {
		document.addEventListener("scroll", this.handleScroll);
		// 포트폴리오 store에 저장하기
		this.getPortfolios();
		// 포스트 store에 저장하기
		this.getPosts();
		this.pushMessaging();
	},
	beforeDestroy() {
		document.removeEventListener("scroll", this.handleScroll);
	}
}
</script>

<style>
#app {
	font-family : 'Avenir', Helvetica, Arial, sans-serif;
	font-size : 1rem;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: #2c3e50;
}

@media (min-width: 24em) {
	:root {
		font-size: calc(1rem + ((1vw - 0.48rem) * 1.7889));
	}
}

@media (min-width: 120em) {
	:root {
		font-size: 1em;
	}
}

.btn-color {
	background: #ffffff;
}

.v-btn--bottom:not(.v-btn--absolute) {
    bottom: 96px;
	right: 21px;
}
</style>

<style src="../static/css/newpage.css"></style>
