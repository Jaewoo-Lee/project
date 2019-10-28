<template>
    <v-container>
        <!-- Comment List -->
        <v-layout>
            <ul style="width:100%; list-style-type:none;">
				<hr>
                <li v-for="comment in getComments" style="margin-top:10px; margin-bottom:10px;">
                    <PortComment v-bind:comment = "comment"/>
					<hr style="margin-top:10px;">
                </li>
            </ul>
        </v-layout>

        <!-- Comment Form -->
		<template v-if="!isGuest">
			<!-- <v-btn flat small @click="show_btn = !show_btn">write</v-btn> -->
			<PortCommentWrite v-show="show_btn" v-bind:portNum="portNum" v-bind:portTitle="portTitle"/>
		</template>
    </v-container>
</template>


<script>
import PortCommentWrite from '@/components/portfolio/PortfolioCommentWrite'
import controller from '@/services/Controller'
import PortComment from '@/components/portfolio/PortfolioComment'

export default {
    name: 'PortCommentList',
    props: ['comments', 'portNum', 'portTitle'],
    data() {
        return {
            show_btn: true
        }
    },
    components: {
        PortComment,
        PortCommentWrite
    },
    computed: {
        getComments: function() {
            return this.comments;
        },
        isGuest: function() {
            if(this.$store.getters.getUser.level == 'GUEST'){
                return true;
            }
            return false;
        }
    },
}
</script>
