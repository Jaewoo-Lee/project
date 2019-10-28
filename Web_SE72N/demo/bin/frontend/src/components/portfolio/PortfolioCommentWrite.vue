<template>
    <form v-on:submit.prevent="writeComment">
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
        <v-btn class="ml-auto" type="submit">등 록</v-btn>
    </form>
</template>


<script>
import controller from '@/services/Controller'

export default{
    props: {
        index: { type: Number },
        portNum: {type: Number},
        portTitle: {type: String}
    },
    data() {
        return {
            commentText : '',
            userId : '',
            portCommentNum : -1
        }
    },
    methods: {
        writeComment: async function() {
            var res = await controller.savePortfolioComment({
                portcommentNum : this.portCommentNum,
                portNum : this.portNum,
                userId : this.$store.getters.getUser.id,
                portcommentContent : this.commentText
			});
			this.commentText = ''

			if(res){
				var list = []
				list = await controller.findToken()
				var title = '포트폴리오 새 댓글 등록'
				var body = '글 제목 : ' + this.portTitle + '\n작성자 : ' + this.$store.getters.getUser.id
				var link = "https://ssafy-se7en.ml/portfolio/"
				controller.sendNotification(list, title, body, link)
			}
        }

    },
    mounted() {
        this.userId = this.$store.getters.getUser.id;
    }
}
</script>

<style>
.st-position {
	/* min-height:200vh; */
	position:initial !important;
}
</style>
