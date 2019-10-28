<template>
	<form v-on:submit.prevent="writeComment">
		<!-- <p>댓글 작성  --  {{userId}}</p> -->
		<v-textarea
		outlined
		filled
		v-model="commentText"
		label="댓글 작성"
		:rows="3"
		:cols="50"
		:auto-grow="true"
		background-color="#ececf1"
		></v-textarea>
		<!-- <input type="submit" value="등록"/> -->
		<v-btn class="ml-auto" type="submit">등 록</v-btn>
	</form>
</template>


<script>
import controller from '@/services/Controller'

export default{
	props: {
		index: { type: Number },
		postNum: { type: Number },
		postTitle: {type: String}
	},
	data() {
		return {
			commentText : '',
			userId : '',
			postCommentNum : -1,
		}
	},
	methods: {
		writeComment: async function() {
			var res = await controller.savePostComment({
				postcommentNum : this.postCommentNum,
				postNum : this.postNum,
				userId : this.$store.getters.getUser.id,
				postcommentContent : this.commentText
			});
			this.commentText = ''
			if(res){
				var list = []
				list = await controller.findToken()
				var title = '포스트 새 댓글 등록'
				var body = '글 제목 : ' + this.postTitle + '\n작성자 : ' + this.$store.getters.getUser.id
				var link = "https://ssafy-se7en.ml/post/"
				controller.sendNotification(list, title, body, link)
			}
		}
	},
	mounted() {
		this.userId = this.$store.getters.getUser.id;
	}
}
</script>
