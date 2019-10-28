<template>
    <v-container>
        <!-- Comment List -->
        <v-layout>
            <ul style="width:100%; list-style-type:none;">
                <hr>
                <li v-for="comment in getComments" style="margin-top:10px; margin-bottom:10px;">
                    <PostComment v-bind:comment = "comment"/>
                    <hr style="margin-top:10px;">
                </li>
            </ul>
        </v-layout>

        <!-- Comment Form -->
        <template v-if="!isGuest">
            <v-btn flat small @click="show_btn = !show_btn">write</v-btn>
            <PostCommentWrite v-show="show_btn" v-bind:postNum="postNum" v-bind:postTitle="postTitle"/>
        </template>
    </v-container>
</template>


<script>
import controller from '@/services/Controller'
import PostComment from '@/components/post/PostComment'
import PostCommentWrite from '@/components/post/PostCommentWrite'

export default {
    name: 'PostCommentList',
    props: ['comments', 'postNum', 'postTitle'],
    data() {
        return {
            show_btn: true,
        }
    },
    components : {
        PostComment,
        PostCommentWrite
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
        },
    },
}
</script>
