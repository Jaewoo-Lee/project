<template>
	<div class="st-container st-position">

		<input type="radio" name="radio-set"  id="st-control-1" v-on:click="gotohome"/>
		<a href="#st-panel-4">HOME</a>

		<input type="radio" name="radio-set" id="st-control-2" v-on:click="gotoportfolio"/>
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
				<!-- Post Detail -->
				<v-container>
					<v-responsive class="mt-top">
						<!-- Post Detail -->
						<v-container fill-height id="st-animation1">
							<v-layout column>
								<v-flex>
									<div style="float:left;">
										<h1> {{title}}</h1>
									</div>
									<div style="float:right;">
										<span>{{userId}}</span>
									</div>
									<br><br>
									<span class="grey--text">{{created_at}}</span>
									<span style="float:right;" v-if="isMember">
										<template v-if="this.$store.getters.getUser.level == 'ADMIN' && this.$store.getters.getUser.id == getUserId">
											<!-- 수정 시에는 현재 가지고 있는 정보를 가지고 PostwriterPage를 호출한다. -->
											<router-link
											:to="{ name: 'postwriter', params: {
												check : true,
												num : getNum,
												title : getTitle,
												content : getBody
												}}" style="color:black; text-decoration: none;">수정</router-link>
										</template>
											<!-- 삭제 시에는 정말 삭제할 건지 한 번 더 물어본다. -->
										<button v-on:click="deletePost">삭제</button>
									</span>

									<v-divider class="my-3"></v-divider>

										<!-- 마크 다운 추가 -->
									<markdown-it-vue class="md-body" :content="body"/>
								</v-flex>
									<!-- Comment List -->
								<v-layout column>
									<v-flex>
										<v-btn flat small @click="show_btn = !show_btn" style="margin-top:100px;">Comments</v-btn>
										<PostCommentList v-show="show_btn" v-bind:comments="getComments" v-bind:postNum="postNum" v-bind:postTitle="getPostTitle"></PostCommentList>
									</v-flex>
								</v-layout>
							</v-layout>
						</v-container>
					</v-responsive>
				</v-container>
			</section>

			<section class="st-panel st-color" id="st-panel-4">
				<div class="st-deco" data-icon="">LOGIN</div>
			</section>
		</div>
	</div>
</template>

<script>
import 'markdown-it-vue/dist/markdown-it-vue.css'
import PostList from "@/components/post/PostList";
import PortfolioList from "@/components/portfolio/PortfolioList";
import PostCommentList from '@/components/post/PostCommentList'
import { isString } from "util";
import MarkdownItVue from 'markdown-it-vue'
import controller from '@/services/Controller'
import router from '@/router/index'

export default {
	name: "DetailPortfolio",
	components: {
		MarkdownItVue,
		PostList,
		PostCommentList,
		PortfolioList
	},
	data() {
		return {
			index : -1,
			postNum : 0,
			title : '',
			body : '',
			textTitle : '',
			textBody : '',
			created_at : '',
			userId : '',
			show_btn: true,
			comments: [],
			tempList : this.$store.getters.getPosts[this.$route.params.id - 1],
		}
	},
	methods: {
		// 포스트 글 삭제하기
		async deletePost(){
			let flag = confirm('정말 삭제하실 건가요? 정말?')
			if(flag){
				await controller.deletePost(this.postNum);
			}
		},

		// 포트폴리오 댓글 삭제하기
		async deletePostComment(num){
			let flag = confirm('정말 댓글을 삭제하실 건가요? 정말?')
			if(flag) {
				await controller.deletePostComment(num);
			}
		},

		// 수정 및 삭제할 권한이 있는지 확인
		isGuest(){
			if(this.$store.getters.getUser.level == 'GUEST'){
				return true;
			}
			return false;
		},
		setTempList() {
			this.comments = this.tempList.commentList
			this.title = this.tempList.postTitle;
			this.body = this.tempList.postContent;
			this.created_at = this.tempList.postDatetime;
			this.userId = this.tempList.userId;
			this.postNum = this.tempList.postNum;
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
		getComments(){
			return this.$store.getters.getPosts[this.$route.params.id - 1].commentList;
		},
		getPostTitle() {
			return this.title;
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
.mt-top{
	margin-top:5rem;
}
.st-position {
	/* min-height:200vh; */
	position:initial !important;
}
#st-animation1 button,
#st-animation1 div,
#st-animation1 li,
#st-animation1 h1,
#st-animation1 h2,
#st-animation1 h3,
#st-animation1 h4,
#st-animation1 h5,
#st-animation1 h6,
#st-animation1 pre,
#st-animation1 ul
{
	-webkit-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-moz-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-o-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-ms-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	animation: moveDown 0.6s ease-in-out 0.2s backwards;
}
</style>
