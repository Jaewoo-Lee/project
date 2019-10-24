<template>
    <v-layout py-4 h-100 >
    <v-hover>
        <!--
        <v-card :to="{name: 'detailport', params: {id: id}}" slot-scope="{ hover }" :class="`elevation-${hover ? 12 : 0}`">
            <v-img :src="imgSrc" height="200px">
            </v-img>
            <v-card-title primary-title>
                <div class="txt-boundary">
                    <div class="headline txt-title">{{title}}</div>
                    <span class="grey--text txt-limit">{{body}}</span>
                </div>
            </v-card-title>
        </v-card>
        -->
        <!-- $vuetify.breakpoint.xs?:3 -->
        <template v-if="imgSrc == 'http://dy.gnch.or.kr/img/no-image.jpg'">
            <div class="box">
                <a class="textLink" v-on:click="goDetail()">
                <div class="boxTop">
                    <div>{{userId}}</div>
                    <div>{{cutDate(date)}}</div>
                </div>
                <div class="boxCenter txt-boundary">
                    <div class="boxTitle txt-title"><a class="textLink" v-on:click="goDetail()">{{title}}</a></div>
                    <div class="boxContent txt-limit"><a class="textLink" v-on:click="goDetail()">{{body}}</a></div>
                </div>
                <div class="boxBottom">
                    <div class="boxBottomTag"><a class="textLink" v-on:click="goDetail()">댓글</a></div>
                </div>
                </a>
            </div>
        </template>
        <template v-else>
            <div class="box2">
                 <a class="textLink" v-on:click="goDetail()">
                    <div class="box2Dan1">
                        <img :src="imgSrc" class="box2Img"/>
                    </div>
                    <div class="box2Dan2">
                        <div class="box2Top">
                            <div>{{userId}}</div>
                            <div>{{cutDate(date)}}</div>
                        </div>
                        <div class="box2Center txt-boundary">
                            <div class="box2Title txt-title">{{title}}</div>
                            <div class="box2Content txt-limit">{{body}}</div>
                        </div>
                        <div class="box2Bottom">
                            <div class="box2BottomTag"><a class="textLink" v-on:click="goDetail()">댓글</a></div>
                        </div>
                    </div>
                </a>
            </div>

        </template>
    </v-hover>
    </v-layout>
</template>


<script>
export default {
    name: 'Portfolio',
    props: {
        id: { type: Number },
        date: {type: String},
        title: {type: String},
        body: {type: String},
        imgSrc: {type: String},
        userId: {type: String}
    },
    data() {
        return {
            portfolio:{
                title:"{{title}}",
            }
        }
    },
    methods:{
        changeBody:function(text){
            this.body = text.replace(/!\[\]\(https\:\/\/i.imgur.com\/[^]*.[^]*g\)/gi,"")
        },
        cutDate: function(text){
            return text.substring(0, 10)
        },
        goDetail: function() {
            this.$router.push({name: 'detailport', params: {id: this.id}})
        }
    },
}
</script>


<style>
.mt-port{
    margin-left:100px;
    margin-right:100px;
}
.txt-boundary {
    /* 제목을 한줄로 표시하려고 하는데 한줄로 표시하면 범위를 벗어나게되서 내용까지 벗어나게됨 */
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    -webkit-line-clamp: 1;
}
.txt-title{
    text-overflow: ellipsis;
    overflow: hidden;
}
.txt-limit {
    white-space: normal;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    word-break:break-all;
    -webkit-box-orient: vertical;
    line-height: 1.2em;
    height: 4.8em;
    /* 4줄 4.8em 3줄 3.6em */
}
.box {
    border : 1px solid gray;
    padding : 20px;
    margin : 20px;
    border-radius: 15px;
    width : 100%;
    height : 283px;
}
.boxTop {
    font-size : 12px;
    margin-bottom : 10px;
    margin-left : 10px;
}
.boxCenter {
    margin-left : 15px;
}
.boxTitle {
    font-size : 25px;
}
.boxContent {
    margin-top : 8px;
    margin-left : 2px;
    margin-bottom : 30px;
    padding-right : 10%;
    font-size : 15px;
}
.boxBottom {
    margin-right : 10px;
    margin-left : 10px;
    font-size : 12px;
    border-top : 1px solid black;
}
.boxBottomTag {
    display : inline-block;
    margin-right : 20px;
}
.textLink {
    text-decoration: none;
    color : black;
}
.box2 {
    margin : 20px;
    border : 1px solid gray;
    overflow: hidden;
    border-radius: 15px;
    width : 100%;
    height : 283px;
}
.box2Top {
    font-size : 12px;
    margin-bottom : 10px;
    margin-left : 10px;
}
.box2Center {
    margin-left : 15px;
}
.box2Title {
    font-size : 25px;
}
.box2Content {
    margin-top : 8px;
    margin-left : 2px;
    margin-bottom : 30px;
    padding-right : 10%;
    font-size : 15px;
}
.box2Bottom {
    margin-right : 10px;
    margin-left : 10px;
    font-size : 12px;
    border-top : 1px solid black;
}
.box2BottomTag {
    display : inline-block;
    margin-right : 20px;
}
.box2Img {
    width : auto;
    height : 100%;
    min-width: 310px;
}
.box2Dan1 {
    width : 48%;
    height : 283px;
    overflow: hidden;
    background-color : white;
    float : left;
}
.box2Dan2 {
    width : 48%;
    float : right;
    padding-left : 2%;
    padding-right : 2%;
    padding-top : 35px;
    padding-bottom : 35px;
}
</style>
