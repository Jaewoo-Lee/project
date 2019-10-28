import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import PostPage from '@/views/PostPage.vue'
import PortfolioPage from '@/views/PortfolioPage.vue'
import PortfoliowriterPage from '@/views/PortfoliowriterPage.vue'
import PostwriterPage from '@/views/PostwriterPage.vue'
import LoginPage from '@/views/LoginPage.vue'
import DetailPortfolio from '@/views/DetailPortfolio.vue'
import DetailPost from '@/views/DetailPost.vue'
import AdminPage from '@/views/AdminPage.vue'
import store from '@/store'
import NotFound from '@/views/NotFound.vue'
import controller from '@/services/Controller'
import VueAnalytics from 'vue-analytics'

Vue.use(Router)

export default new Router({
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomePage,
            // beforeEnter: function(to, from, next){
			// 	controller.saveLog('HomePage')
            //     next()
            // }
        },
        {
            path: '/post',
            name: 'post',
            component: PostPage,

            // beforeEnter: function(to, from, next){
			// 	controller.saveLog('PostPage')
            //     next()
            // }
        },
        {
            path: '/portfolio/write',
            name: 'portfoliowriter',
            component: PortfoliowriterPage,
            beforeEnter: function(to, from, next){
				if(store.getters.getUser.level == 'GUEST'){
					alert("로그인 하고 와라")
					next('/')
				} else {
					next()
				}
            }
		},
		{
			 path: '/post/write',
            name: 'postwriter',
            component: PostwriterPage,
            beforeEnter: function(to, from, next){
				if(store.getters.getUser.level == 'GUEST'){
					alert("로그인 하고 와라")
					next('/')
				} else {
					next()
				}
            }
		},
        {
            path: '/portfolio',
            name: 'portfolio',
            component: PortfolioPage,
            // beforeEnter: function(to, from, next){
			// 	controller.saveLog('PortfolioPage')
            //     next()
            // }
        },
        {
            path: '/portfolio/:id',
            name: 'detailport',
            component: DetailPortfolio,
            // beforeEnter: function(to, from, next){
			// 	controller.saveLog('DetailPortfolio')
            //     next()
            // }
        },
        {
            path: '/post/:id',
            name: 'detailpost',
            component: DetailPost,
            // beforeEnter: function(to, from, next){
			// 	controller.saveLog('DetailPost')
            //     next()
            // }
        },
        {
            path: '/login',
            name: 'login',
            component: LoginPage,
            // beforeEnter: function(to, from, next){
			// 	controller.saveLog('HomePage')
            //     next()
            // }
        },
        {
            path: '*',
            name: 'notfound',
            component: NotFound
        },
        {
            path: '/admin',
            name: 'admin',
            component: AdminPage,
            beforeEnter: function(to, from, next){
                if(store.getters.getUser.level != 'ADMIN'){
                    alert("비정상적인 접근입니다." + store.getters.getUser.level)
                    return next('/');
                }
                next();
            }
        },
    ],
    scrollBehavior (to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return { x: 0, y: 0 }
        }
    }
})

Vue.use(VueAnalytics, {
    id: 'UA-145146446-1'
})
