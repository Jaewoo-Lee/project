<template>
	<div>
		<div class="st-container">

			<input type="radio" name="radio-set"  id="st-control-1" v-on:click="gotohome"/>
			<a href="#st-panel-4">HOME</a>

			<input type="radio" name="radio-set"  id="st-control-2" v-on:click="gotoportfolio"/>
			<a href="#st-panel-4">PORTFOLIO</a>

			<input type="radio" name="radio-set" checked="checked" id="st-control-3" v-on:click="gotopost"/>
			<a href="#st-panel-3">POST</a>

			<input type="radio" name="radio-set" id="st-control-4" v-on:click="gotologin"/>
			<a href="#st-panel-4">LOGIN</a>

			<div class="st-scroll">

				<section class="st-panel" id="st-panel-1">
					<div class="st-deco" data-icon="">HOME</div>
				</section>

				<section class="st-panel st-color" id="st-panel-2">
					<div class="st-deco" data-icon="">PORTFOLIO</div>
					<PortfolioList></PortfolioList>
				</section>

				<section class="st-panel" id="st-panel-3">
					<div class="st-deco" data-icon="">POST</div>
					<PostList></PostList>
				</section>

				<section class="st-panel st-color" id="st-panel-4">
					<div class="st-deco" data-icon="">LOGIN</div>
				</section>
			</div>

		</div>
	</div>
</template>


<script>
import PostList from '@/components/post/PostList'
import PortfolioList from '@/components/portfolio/PortfolioList'
import { page } from 'vue-analytics'
import router from '@/router/index'

export default {
	name: 'PostPage',
	components: {
		PostList,
		PortfolioList
	},
	props: {
		id: { type: Number },
		date: { type: String },
		title: { type: String },
		body: { type: String },
		imgSrc: { type: String }
	},
	methods:{
		gotohome(){
			setTimeout(function() {
				console.log('홈으로 가자');
				router.push({name: 'home'})
			}, 600);
		},
		gotopost(){
			setTimeout(function() {
				router.push({name: 'post'})
			}, 600);
		},
		gotoportfolio(){
			setTimeout(function() {
				router.push({name: 'portfolio'})
			}, 600);
		},
		gotologin(){
			setTimeout(function() {
				router.push({name: 'login'})
			}, 600);
		}
	}
	// methods: {
	// 	track () {
	// 		page({
	// 			page: '/post',
	// 			title: 'Post Page',
	// 			location: window.location.href
	// 		})
	// 	}
	// }
}
</script>


<style>
.hooper-indicator {
  background-color: #E6E6E6;
}
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h1,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h2,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h3,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h4,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h5,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h6,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing p,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing div,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing span,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing pre,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing ul,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing li,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing h1,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing h2,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing h3,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing h4,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing h5,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing h6,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing p,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing div,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing span,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing pre,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing ul,
#st-control-3:checked ~ .st-scroll #st-panel-3-nothing li
{
	-webkit-animation: initial;
	-moz-animation: initial;
	-o-animation: initial;
	-ms-animation: initial;
	animation: initial;
}

</style>
