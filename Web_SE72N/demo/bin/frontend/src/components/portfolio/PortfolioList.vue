<template>
   <v-layout row wrap mw-1400 style="margin-top:20vh;" >

        <hooper :settings="hooperSettings" :itemsToShow="$vuetify.breakpoint.xs?1:2"  style="height:100%;" id="st-panel-content-nothing">

            <slide v-for="i in portfolios.length" class="mx-slide" :key="i">
                <p></p>
                <Portfolio class="word-boundary ma-3"
                    :id="i"
                    :date="portfolios[i - 1].portDatetime"
                    :title="portfolios[i - 1].portTitle"
                    :body="changeBody(portfolios[i - 1].portContent)"
                    :imgSrc="portfolios[i - 1].portImg"
                    :userId="portfolios[i - 1].userId"
                    ></Portfolio>
            </slide>
            <hooper-pagination slot="hooper-addons"></hooper-pagination>
            <hooper-navigation slot="hooper-addons"></hooper-navigation>
        </hooper>

            <router-link :to="{ name: 'portfoliowriter', params: { check : false}}" style="color:white; font-weight:bold" class="mx-auto">
                <v-btn class="login_btn" outlined dark large color="rgb(120,144,156)" v-if="isAvailable">
                WRITE
                </v-btn>
            </router-link>
<!--
       <v-flex v-for="i in portfolios.length > getLimits ? getLimits : portfolios.length" md3 sm6 xs12>
           <Portfolio class="ma-3 word-boundary"
           :id="i"
           :date="portfolios[i - 1].portDatetime"
           :title="portfolios[i - 1].portTitle"
           :body="changeBody(portfolios[i - 1].portContent)"
           :imgSrc="portfolios[i - 1].portImg"
           ></Portfolio>
       </v-flex>
       <v-flex xs12 text-xs-center round my-5 v-if="isShow">
               <v-btn color="rgba(182, 198, 207, 1)" dark v-on:click="loadMorePortfolios"><v-icon size="25" class="mr-2">fa-plus</v-icon> 더 보기</v-btn>
       </v-flex> -->
   </v-layout>
</template>


<script>
import 'hooper/dist/hooper.css';
import Portfolio from '@/components/portfolio/Portfolio'
import controller from '@/services/Controller'
import { Hooper, Slide,  Navigation as HooperNavigation, Pagination as HooperPagination } from 'hooper';
export default {
    name: 'PortfoliosList',
    props: {
        limits: {type: Number, default: 4},
        loadMore: {type: Boolean, default: false}
    },
    data() {
        return {
            limitHere : this.limits,
            hooperSettings : {
                transition:500
            }
        };
    },
    components: {
        Portfolio,
        Hooper,
        Slide,
        HooperPagination,
        HooperNavigation
    },
    computed: {
        portfolios : function() {
            return this.$store.getters.getPortfolios
        },
        isAvailable: function() {
            // if(this.loadMore){
            const level = this.$store.getters.getUser.level
            //console.log(level)

            if(level == 'ADMIN' || level == 'MEMBER'){

                return true
            }
            // }
            return false
        },
        getLimits : function() {
            return this.limitHere;
        },
        isShow: function() {
            if(this.loadMore){
                if(this.getLimits < this.portfolios.length){
                    return true
                }
            }
            return false
        }
    },
    methods: {
        loadMorePortfolios() {
            this.limitHere += 4
        },
        changeBody:function(text){
            return text.replace(/!\[\]\(https\:\/\/i.imgur.com\/[^]*.[^]*g\)/gi,"").replace(/#/gi, '')
        },

        async getPortfolios(){
            await controller.getPortfolios()
        }
    },
    mounted(){
        this.hooperSettings.transition = 300
        this.getPortfolios()
    }
}
</script>


<style>
.mt-port{
    margin-top : 20vh;
    height:65%;
    bottom : 0;
}
.mx-slide{
    margin-bottom: 15px;
}
.mw-700 {
    max-width: 700px;
    margin: auto;
}
.word-boundary{
    word-wrap: break-word;
}
li.mx-slide.hooper-slide {
    /* width: 20%!important; */
    min-width: 212px;
}
.hooper-indicator {
    background-color: #CCCCCC !important;
}
.hooper-indicator:hover, .hooper-indicator.is-active {
    background-color: #4285f4 !important;
}
#st-panel-content-nothing h1,
#st-panel-content-nothing h2,
#st-panel-content-nothing h3,
#st-panel-content-nothing h4,
#st-panel-content-nothing h5,
#st-panel-content-nothing h6,
#st-panel-content-nothing p,
#st-panel-content-nothing div,
#st-panel-content-nothing span,
#st-panel-content-nothing pre,
#st-panel-content-nothing ul,
#st-panel-content-nothing li{
    -webkit-animation: initial;
    -moz-animation: initial;
    -o-animation: initial;
    -ms-animation: initial;
    animation: initial;
}
</style>
