<template>
	<div class="st-container st-position">

		<input type="radio" name="radio-set" id="st-control-1" v-on:click="gotohome"/>
		<a href="#st-panel-4">HOME</a>

		<input type="radio" name="radio-set" checked="checked" id="st-control-2" v-on:click="gotoportfolio"/>
		<a href="#st-panel-4">PORTFOLIO</a>

		<input type="radio" name="radio-set" id="st-control-3" v-on:click="gotopost"/>
		<a href="#st-panel-3">POST</a>

		<input type="radio" name="radio-set"  id="st-control-4" v-on:click="gotologin"/>
		<a href="#st-panel-4">LOGIN</a>

		<div class="st-scroll">

			<section class="st-panel" id="st-panel-1">
				<div class="st-deco" data-icon="">HOME</div>
			</section>

			<section class="st-panel st-color st-panel-2-write">
				<div class="st-deco" data-icon="">PORTFOLIO</div>

				<v-container style="margin-top:20vh;" id="st-panel-2-write-content">
					<div style="text-align:left; width:100%; font-size:25px;">제목:
						<input type="text" v-model="portitle" style="border:black solid 1px; width:90%; background-color:#e6f3ff" placeholder="제목없음"/>
					</div>
					<br>
					<v-layout row wrap>
						<v-flex md6>
							<h2>Markdown Preview</h2>
							<markdown-it-vue class="md-body" :content="content"/>
						</v-flex>

						<v-flex md6>
							<markdown-editor v-model="content" ref="markdownEditor"></markdown-editor>
							<ImgUploader :parent-message="parentMessage" @send-message="getChildMessage">
							</ImgUploader>

							<v-flex class="d-flex justify-center">
								<v-btn color="rgba(182, 198, 207, 1)" class="white--text" depressed @click="submit">Submit</v-btn>
							</v-flex>
						</v-flex>
					</v-layout>
				</v-container>
			</section>

			<section class="st-panel" id="st-panel-3">
				<div class="st-deco" data-icon="">POST</div>
				<PostList></PostList>
			</section>

			<section class="st-panel st-color" id="st-panel-4">
				<div class="st-deco" data-icon=""></div>
			</section>
		</div>

	</div>
</template>


<script>
import MarkdownItVue from 'markdown-it-vue'
import 'markdown-it-vue/dist/markdown-it-vue.css'
import PortfolioList from '@/components/portfolio/PortfolioList'
import markdownEditor from 'vue-simplemde/src/markdown-editor'
import ImgUploader from '@/components/ImgUploader'
import controller from '@/services/Controller'
import router from '@/router/index'
import PostList from '@/components/post/PostList'

export default {
	name: 'PortfoliowriterPage',
	components: {
		PortfolioList,
		MarkdownItVue,
		markdownEditor,
		ImgUploader,
		PostList
	},
	data() {
		return {
			num: -1,
			content: '# This is markdown editor!!',
			childMessage:'',
			firstimage:'http://dy.gnch.or.kr/img/no-image.jpg',
			parentMessage:'이것은 부모 데이터이다',
			portTitle: '무제',
			portitle : '',
		}
	},
	mounted() {
		if(this.$route.params.check){
			this.num = this.$route.params.num
			this.content = this.$route.params.content
			this.portitle = this.$route.params.title
		}
	},
	methods:{
		getChildMessage: function(text) {
			this.childMessage = text
			this.content += text
		},
		submit : async function(content){
			if(this.portitle == null){
				this.portTitle = '무제'
			}
			this.firstimage = this.content.match(/https\:\/\/i.imgur.com\/[^]*.[^]*g/)
			if (this.firstimage === null){
				this.firstimage = ["http://dy.gnch.or.kr/img/no-image.jpg"];
			}

			var res = controller.savePortfolio(this.num, this.portitle, this.content, this.firstimage[0]);
			if(this.num == -1 && res) {	// 글이 저장되었는데 새로 작성한 거면 푸쉬를 보내기
				var list = []
				list = await controller.findToken()
				var title = '포트폴리오 새 글 등록'
				var body = '제목 : ' + this.portitle + '\n작성자 : ' + this.$store.getters.getUser.id
				controller.sendNotification(list, title, body)
			}
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
	watch:{
		content:function(val){
			// console.log(val)
		}
	}
}
</script>


<style>
@import 'simplemde/dist/simplemde.min.css';

.btn-color {
	background: linear-gradient(
		to right,
		rgb(255, 255, 0),
		rgb(252, 100, 73)
	);
}
.st-position {
	/* min-height:200vh; */
	position:initial !important;
}
.st-panel-2-write{
	-webkit-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-moz-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-o-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	-ms-animation: moveDown 0.6s ease-in-out 0.2s backwards;
	animation: moveDown 0.6s ease-in-out 0.2s backwards;
}

#st-control-2:checked ~ .st-scroll #st-panel-2-write-content h1,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content h2,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content h3,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content h4,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content h5,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content h6,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content p,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content div,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content span,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content pre,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content ul,
#st-control-2:checked ~ .st-scroll #st-panel-2-write-content li
{
	-webkit-animation: initial;
	-moz-animation: initial;
	-o-animation: initial;
	-ms-animation: initial;
	animation: initial;
}


</style>
