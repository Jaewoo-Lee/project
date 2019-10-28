<template>
	<div>
		<template v-if="!show_update">
			<div style="float:left;">
				{{getUserId}}<br>   {{getCommentDatetime}}<br>
			</div>
			<div style="float:right;">

			</div>

			<div style="float:left;">

			</div>
			<div style="float:right;">

				<template v-if="isMember && getId == getUserId">
					<button v-on:click="updatePostComment(getCommentNum)">수정</button>
				</template>
				<template v-if="getLevel == 'ADMIN' || (!isGuest && getId == getUserId)">
					<button v-on:click="deletePostComment(getCommentNum)">삭제</button>
				</template>
			</div>


			<br>
			<br>>> {{getCommentContent}}
		</template>
		<template v-else>
			<!-- 수정하는 입력 폼 넣고 -->
			<form v-on:submit.prevent="writeComment" style="width:100%;">
				<v-textarea
				outlined
				filled
				v-model="commentText"
				label="댓글 작성"
				:rows="3"
				:cols="50"
				:auto-grow="true"
				background-color="#F8F8F8"
				></v-textarea>
				<!-- <input type="submit" value="등록"/> -->
				<v-btn class="ml-auto" type="submit">수 정</v-btn>
				<v-btn class="ml-auto" @click="cancelComment">취 소</v-btn>
			</form>
		</template>
	</div>
</template>


<script>
import controller from '@/services/Controller'

export default {
	name: 'PostComment',
	props: ['comment'],
	data(){
		return{
			postNum : 0,
			show_update : false,
			commentText : ''
		}
	},
	computed : {
		isGuest: function() {
			if(this.$store.getters.getUser.level == 'GUEST'){
				return true;
			}
			return false;
		},
		getId: function() {
			return this.$store.getters.getUser.id
		},
		getLevel: function() {
			return this.$store.getters.getUser.level
		},
		getCommentContent: function() {
			return this.comment.postcommentContent
		},
		getCommentDatetime: function() {
			return this.comment.postcommentDatetime.replace('T', ' ').substring(0, 16)
		},
		getUserId: function() {
			return this.comment.userId
		},
		getCommentNum: function() {
			return this.comment.postcommentNum
		},
		isMember: function() {
			const level = this.$store.getters.getUser.level
			if(level == 'MEMBER' || level == 'VISITOR'){
				return true
			}
			return false
		}
	},
	methods:{
		// 댓글 삭제하기
		async deletePostComment(num){
			let flag = confirm('정말 댓글을 삭제하실 건가요? 정말?')
			if(flag) {
				await controller.deletePostComment(num);
			}
		},
		// 댓글 수정하는 폼 보이게
		updatePostComment(num) {
			this.show_update = true
		},
		// 댓글 수정하기
		async writeComment() {
			await controller.savePostComment({
				postcommentNum : this.getCommentNum,
				postNum : this.postNum,
				userId : this.$store.getters.getUser.id,
				postcommentContent : this.commentText
			});
			this.show_update = false
		},
		// 댓글 수정 취소
		cancelComment(){
			this.show_update = false
			this.commentText = this.getCommentContent
		}
	},
	mounted(){
		this.postNum = this.comment.postNum
		this.commentText = this.getCommentContent
	}
}
</script>
