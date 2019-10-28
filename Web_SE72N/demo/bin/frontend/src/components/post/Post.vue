<template>
    <v-layout py-4 h-100 >
        <v-hover>
            <!-- <v-card
            :to="{name: 'detailpost', params: {id: id}}"
            slot-scope="{ hover }"
            :class="`elevation-${hover ? 12 : 0}`"
			style="width:100%;">
                <v-card-title primary-title>
                    <div class="txt-boundary">
                        <div class="headline txt-title">{{dtitle}}</div>
                        <span class="grey--text txt-limit">{{dbody}}</span>
                    </div>
                </v-card-title>
            </v-card> -->

                <div class="box">
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
            </div>

        </v-hover>
    </v-layout>
</template>


<script>
export default {
    name: 'Post',
    props: {
        id: {type: Number},
        date: {type: String},
        title: {type: String},
        body: {type: String},
        comments: {type: Array},
        tran : {type: Number},
        userId: {type: String}
    },
    data(){
        return{
            dtitle : '',
            dbody : '',
        }
    },
    methods:{
        cutDate: function(text){
            return text.substring(0, 10)
        },
        goDetail: function() {
            this.$router.push({name: 'detailpost', params: {id: this.id}})
        }
    },
    mounted(){
        this.dtitle = this.title;
        this.dbody = this.body;
    }
}
</script>


<style>
.color-666 {
    color: #666;
}
.color-333 {
    color: #333;
}
.h-100 {
    height: 100%;
}
.txt-boundary {
    /* 제목을 한줄로 표시하려고 하는데 한줄로 표시하면 범위를 벗어나게되서 내용까지 벗어나게됨 */
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    -webkit-line-clamp: 1;
    padding: 7px;
    /* word-wrap: break-word; */
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
    /* word-wrap: break-word; */
    line-height: 1.2em;
    height: 4.8em;
    /* 4줄 4.8em 3줄 3.6em */
}
.txt-limit:hover {
    overflow: visible;
    text-overflow: visible;
    -webkit-line-clamp: none;
    word-break:none;
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
</style>
