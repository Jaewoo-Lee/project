<template>
    <v-layout row wrap mw-1400 style="margin-top:20vh;">

        <hooper :itemsToShow="$vuetify.breakpoint.xs?1:2" :transition="500" style="height:100%;">
            <slide v-for="i in posts.length" class="mx-slide">
                <Post class="ma-3 word-boundary"
                :id="i"
                :date="posts[i - 1].postDatetime"
                :title="posts[i - 1].postTitle"
                :body="changeBody(posts[i - 1].postContent)"
                :userId="posts[i-1].userId"
                ></Post>
            </slide>
            <hooper-navigation slot="hooper-addons"></hooper-navigation>
            <hooper-pagination slot="hooper-addons"></hooper-pagination>
        </hooper>

        <router-link :to="{ name: 'postwriter', params: { check : false}}" style="color:white; font-weight:bold; text-decoration:none;" class="mx-auto">
            <v-btn class="login_btn" outlined dark large color="rgb(120,144,156)" v-if="isAvailable">
                WRITE
            </v-btn>
        </router-link>

    </v-layout>
</template>


<script>
import 'hooper/dist/hooper.css';
import Post from '@/components/post/Post'
import { Hooper, Slide,  Navigation as HooperNavigation, Pagination as HooperPagination } from 'hooper';
import controller from '@/services/Controller'

export default {
    name: 'PostList',
    props: {
        column: {type: Number, default: 1},
        limits: {type: Number, default: 4},
        loadMore: {type: Boolean, default: false}
    },
    data() {
        return {
            tran : 0,
            limitHere : this.limits
        }
    },
    components: {
        Post,
        Hooper,
        Slide,
        HooperPagination,
        HooperNavigation
    },
    computed: {
        posts : function() {
            return this.$store.getters.getPosts
        },
        isAvailable : function() {
            // if(this.loadMore){
            const level = this.$store.getters.getUser.level
            if(level == 'ADMIN' || level == 'MEMBER'){
                return true
            }
            // }
            return false
        },
        getLimits: function() {
            return this.limitHere;
        },
        isShow: function() {
            if(this.loadMore){
                if(this.getLimits < this.posts.length){
                    return true
                }
            }
            return false
        }
    },
    methods: {
        loadMorePosts() {
            this.limitHere += 4
        },
        toKo(){
            this.$store.commit('toKo');
            this.tran = 1;
        },
        toEn(){
            this.$store.commit('toEn');
            this.tran = 2;
        },
        changeBody:function(text){
            return text.replace(/!\[\]\(https\:\/\/i.imgur.com\/[^]*.[^]*g\)/gi,"").replace(/#/gi, '')
        },
        async getPosts(){
            await controller.getPosts();
        }
    },
    mounted(){
        this.getPosts()
    }
}
</script>


<style>
.mx-slide{
    /* 여기 왜 아무것도 없지? */
}
.mw-1400 {
    max-width: 1400px;
    margin: auto;
}
.btn-color {
    background: linear-gradient(to right,rgb(252, 174, 73),rgb(255, 230, 8));
}
</style>
