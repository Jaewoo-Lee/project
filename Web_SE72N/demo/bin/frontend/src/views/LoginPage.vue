<template>
	<div>
		<div class="st-container">

			<input type="radio" name="radio-set" id="st-control-1" v-on:click="gotohome"/>
			<a href="#st-panel-4">HOME</a>

			<input type="radio" name="radio-set" id="st-control-2" v-on:click="gotoportfolio"/>
			<a href="#st-panel-4">PORTFOLIO</a>

			<input type="radio" name="radio-set" id="st-control-3" v-on:click="gotopost"/>
			<a href="#st-panel-3">POST</a>

			<input type="radio" name="radio-set" checked="checked" id="st-control-4" v-on:click="gotologin"/>
			<a href="#st-panel-4">LOGIN</a>

			<div class="st-scroll">

				<section class="st-panel" id="st-panel-1">
					<div class="st-deco" data-icon="">HOME</div>
				</section>

				<section class="st-panel st-color" id="st-panel-2">
					<div class="st-deco" data-icon="">PORTFOLIO</div>
					<PortfolioList id="st-panel-2-nothing"></PortfolioList>
				</section>

				<section class="st-panel" id="st-panel-3">
					<div class="st-deco" data-icon="">POST</div>
					<PostList id="st-panel-3-nothing"></PostList>
				</section>

				<section class="st-panel st-color" id="st-panel-4" style="text-align:center;">
					<div class="st-deco" data-icon=""></div>

					<v-layout align-center justify-center column fill-height>
						<template v-if="user.level == 'GUEST'">
							<div style="font-size:30px;margin-top:250px">로그인해주세요</div>
						</template>

						<template v-else>
							<div style="font-size:30px; margin-top:250px;">{{user.id}}님, 안녕하세요!</div>

							<template v-if="user.level == 'ADMIN'">
								<v-btn flat>
									<router-link to="/admin" style="text-decoration:none;color:red"><v-icon small>build</v-icon>AdminPage</router-link>
								</v-btn>
							</template>

							<table style="border: 1px black solid; border-collapse:collapse; margin:40px auto;">
								<tr>
									<th> ID </th>
									<td> {{user.id}} </td>
								</tr>
								<tr>
									<th> LEVEL </th>
									<td> {{user.level}} </td>
								</tr>
								<tr>
									<th> GIT NAME </th>
									<td> {{user.github}} </td>
								</tr>
							</table>
							<br>
						</template>

						<login/>
					</v-layout>

				</section>
			</div>
		</div>
	</div>
</template>


<script>
import PortfolioList from '@/components/portfolio/PortfolioList'
import PostList from '@/components/post/PostList'
import { page } from 'vue-analytics'
import router from '@/router/index'
import FirebaseService from "@/services/FirebaseService"
import controller from "@/services/Controller";
import login from '@/components/login/Login'

export default {
	name: 'LoginPage',
	components: {
		PortfolioList,
		login,
		PostList
	},
	data() {
		return{
			user : {
				level : 'GUEST',
			}
		}
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
		},
	},
	computed:{
		isLogin(){
			return this.$store.getters.getUser;
		},
	},
	mounted(){
		this.user = this.$store.getters.getUser;
	},
	watch:{
		isLogin(val, oldVal){
			this.user = val;
		}
	}
}
</script>


<style scoped>
table td, th {
    font-size: x-large;
    padding: 20px;
}
table th {
    border-right: 3px double black;
    border-collapse: collapse;
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
