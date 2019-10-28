<template>
    <div>
        <v-container>
            <div class="st-container">

                <input type="radio" name="radio-set" checked="checked" id="st-control-1" v-on:click="gotohome"/>
                <a href="#st-panel-4">HOME</a>

                <input type="radio" name="radio-set" id="st-control-2" v-on:click="gotoportfolio"/>
                <a href="#st-panel-4">PORTFOLIO</a>

                <input type="radio" name="radio-set" id="st-control-3" v-on:click="gotopost"/>
                <a href="#st-panel-3">POST</a>

                <input type="radio" name="radio-set" id="st-control-4" v-on:click="gotologin"/>
                <a href="#st-panel-4">LOGIN</a>

                <div class="st-scroll">

                    <section class="st-panel" id="st-panel-1">
                        <div class="st-deco" data-icon="">HOME</div>
                        <img src="https://dvdprime.com/g2/data/cheditor5/1907/mania-done-f9b7a35b62e5464122cb60a9fbcf4d2e_512_286_mp4webm_485-156.gif" style="height:100%; width:100%; z-index=-1;">
                    </section>

                    <section class="st-panel st-color" id="st-panel-2-nothing">
                        <div class="st-deco" data-icon="">PORTFOLIO</div>
                        <PortfolioList></PortfolioList>
                    </section>

                    <section class="st-panel" id="st-panel-3">
                        <div class="st-deco" data-icon="">POST</div>
                        <PostList></PostList>
                    </section>

                    <section class="st-panel st-color" id="st-panel-4">
                        <div class="st-deco" data-icon="">LOGIN</div>
                    </section>
                </div>

            </div>

            <!-- Snackbar -->
            <v-snackbar v-model="snackbar" bottom multi-line right>
                해당 사이트는 크롬에 최적화 되어있습니다.
                <v-btn color="pink" flat @click="snackbar = false">Close</v-btn>
            </v-snackbar>

        </v-container>
    </div>
</template>


<script>
import PortfolioList from '@/components/portfolio/PortfolioList'
import PostList from '@/components/post/PostList'
import router from '@/router/index'
import { page } from 'vue-analytics'

export default {
    name: 'HomePage',
    data() {
        return {
            snackbar: false,
        }
    },
    components: {
        PortfolioList,
        PostList,
    },
    methods: {
        getImgUrl(img) {
            return require('../assets/' + img)
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
        // track () {
        //   page({
        //     page: '/',
        //     title: 'Home page',
        //     location: window.location.href
        //   })
        // }
    },
    computed: {
        prtNum : function() {
            return this.$store.getters.getPortfolios.length
        },
        pstNum : function() {
            return this.$store.getters.getPosts.length
        }
    },
    created() {
        const title = document.title;
        const url = location.href;
        var triggerDefault = false;
        var isChromium = window.chrome,isOpera = window.navigator.userAgent.indexOf("OPR") > -1 || window.navigator.userAgent.indexOf("Opera") > -1;

        if (window.sidebar && window.sidebar.addPanel) {
            //firefox version<23
            console.log("firefox before 23")
            return (this.snackbar = true);
        }else if(isChromium !== null && isOpera == true) {
            // Opera (chromium)
            return (this.snackbar = true);
        }else if ((window.sidebar && (navigator.userAgent.toLowerCase().indexOf('firefox') > -1)) || (window.opera && window.print)) {
            // Firefox version >= 23 and Opera Hotlist
            return (this.snackbar = true);
            console.log("firefox or opera")
        } else if(window.external && ('AddFavorite' in window.external)){
            //IE
            console.log("IE")
            return (this.snackbar = true);
        } else if (document.all) {
            //IE
            return (this.snackbar = true);
        }
    }
}
</script>


<style>
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h1,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h2,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h3,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h4,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h5,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing h6,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing p,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing div,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing span,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing pre,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing ul,
#st-control-2:checked ~ .st-scroll #st-panel-2-nothing li
{
	-webkit-animation: initial;
	-moz-animation: initial;
	-o-animation: initial;
	-ms-animation: initial;
	animation: initial;
}
</style>
