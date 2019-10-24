<template>
	<div class="st-container st-position">

		<input type="radio" name="radio-set"  id="st-control-1" v-on:click="gotohome"/>
		<a href="#st-panel-4">HOME</a>

		<input type="radio" name="radio-set" checked="checked" id="st-control-2" v-on:click="gotoportfolio"/>
		<a href="#st-panel-4">PORTFOLIO</a>

		<input type="radio" name="radio-set" id="st-control-3" v-on:click="gotopost"/>
		<a href="#st-panel-3">POST</a>

		<input type="radio" name="radio-set" id="st-control-4" v-on:click="gotologin"/>
		<a href="#st-panel-4">LOGIN</a>

		<div class="st-scroll">

			<section class="st-panel" id="st-panel-1">
				<div class="st-deco" data-icon="">HOME</div>
			</section>

			<section class="st-panel st-color" id="st-panel-2">
				<div class="st-deco" data-icon="">PORTFOLIO</div>
				<!-- Portfolio Detail -->
				<v-container>
					<v-responsive class="mt-top">
						<v-container fill-height id="st-animation">
							<v-layout column>
								<v-flex>
									<div style="float:left;">
										<h1> {{getTitle}}</h1>
									</div>
									<div style="float:right;">
										<span>{{getUserId}}</span>
									</div>
									<br><br>
									<span class="grey--text">{{getCreatedAt}}</span>

									<span style="float:right;" v-if="isMember">
										<template v-if="this.$store.getters.getUser.level == 'ADMIN' && this.$store.getters.getUser.id == getUserId">
											<!-- 수정 시에는 현재 가지고 있는 정보를 가지고 PortfoliowriterPage를 호출한다. -->
											<router-link :to="{ name: 'portfoliowriter', params: {
												check : true,
												num : this.portNum,
												title : this.title,
												content : this.body }}" style="color:black; text-decoration: none;">수정</router-link>
										</template>
										<!-- 삭제 시에는 정말 삭제할 건지 한 번 더 물어본다. -->
										<button v-on:click="deletePortfolio">삭제</button>
									</span>

									<v-divider class="my-3"></v-divider>

									<!-- 마크 다운 추가 -->
									<markdown-it-vue class="md-body" :content="getBody"/>

									<v-layout column style="margin-bottom:50px;">
										<v-flex>
											<v-btn flat small @click="show_btn = !show_btn" style="margin-top:100px;">Comments</v-btn>
											<PortCommentList v-show="show_btn" v-bind:comments="getComments" v-bind:portNum="portNum" v-bind:portTitle="getTitle"></PortCommentList>
										</v-flex>
									</v-layout>

								</v-flex>
								<!-- Comment List -->

							</v-layout>
						</v-container>
					</v-responsive>
				</v-container>
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
</template>


<script>
import 'markdown-it-vue/dist/markdown-it-vue.css'
import PortfolioList from "@/components/portfolio/PortfolioList";
import PortCommentList from '@/components/portfolio/PortfolioCommentList'
import { isString } from "util";
import router from '@/router/index'
import MarkdownItVue from 'markdown-it-vue'
import controller from '@/services/Controller'
import PostList from '@/components/post/PostList'

export default {
	name: "DetailPortfolio",
	components: {
		MarkdownItVue,
		PortfolioList,
		PortCommentList,
		PostList
	},
	data() {
		return {
			index : -1,
			portNum : 0,
			title : '',
			body : '',
			textTitle : '',
			textBody : '',
			created_at : '',
			img : '',
			userId : '',
			show_btn: true,
			comments: [],
			user : this.$store.getters.getUser,
			tempList : this.$store.getters.getPortfolios[this.$route.params.id - 1]	// 포트폴리오 하나의 내용 전체를 담고 있는 리스트
		}
	},
	methods: {
		// 포트폴리오 글 삭제하기
		async deletePortfolio(){
			let flag = confirm('정말 삭제하실 건가요? 정말?')
			if(flag){
				await controller.deletePortfolio(this.portNum);
			}
		},
		isGuest(){
			if(this.user.level == '' || this.user.level == 'GUEST'){
				return true;
			}
			return false;
		},
		setTempList() {
			this.comments = this.tempList.commentList
			this.title = this.tempList.portTitle;
			this.body = this.tempList.portContent;
			this.created_at = this.tempList.portDatetime;
			this.img = this.tempList.portImg;
			this.userId = this.tempList.userId;
			this.portNum = this.tempList.portNum;
		},
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
	},
	mounted() {
		this.setTempList();
	},
	computed: {
		// 변경되는 데이터들
		changePortfolio(){	// 포트폴리오 내용이 변경되서 들어오면 전체를 바꿔준다.
			this.setTempList();
		},
		getComments(){
			return this.$store.getters.getPortfolios[this.$route.params.id - 1].commentList;
		},
		getTitle(){
			return this.title;
		},
		getBody(){
			return this.body;
		},
		getCreatedAt(){
			return this.created_at;
		},
		getImg(){
			return this.img;
		},
		getUserId(){
			return this.userId;
		},
		isMember(){
			const temp = this.$store.getters.getUser
			if(temp.level == 'ADMIN'){
				return true
			} else if(temp.level == 'MEMBER' && this.userId == temp.id){
				return true
			}
			return false
		}
	}
};
</script>


<style>
.mt-detail{
	/* margin-top : 60px; */
}
.st-position {
	/* min-height:200vh; */
	position:initial !important;
}
.mt-top{
	margin-top:5rem;
}
#st-animation div,
#st-animation li,
#st-animation h1,
#st-animation h2,
#st-animation h3,
#st-animation h4,
#st-animation h5,
#st-animation h6,
#st-animation pre,
#st-animation ul
{
	-webkit-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-moz-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-o-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-ms-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	animation: moveDown 0.6s ease-in-out 0.2s backwards;
}

</style>
