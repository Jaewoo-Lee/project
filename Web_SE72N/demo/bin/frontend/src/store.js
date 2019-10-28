import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        accessToken: '',
        user: {
            level : 'GUEST',
            id : '',
            github : ''
        },
        portfolios:[],
        posts: [],
        source: '',
        target: '',
		imagebannersrc:localStorage.getItem("imagebannersrc"),
		users : [],
        counts : []
    },
    mutations: {
        toEn(state){
            state.source = 'ko'
            state.target = 'en'
        },
        toKo(state){
            state.source = 'en'
            state.target = 'ko'
        },
        logout(state){
            state.accessToken = '';
            state.user = {
               level : 'GUEST',
               id : '',
               github : ''
           }
        },
        login(state, payload){
            state.user.id = payload.id;
            state.user.level = payload.authority;
            state.user.github = payload.github;
        },
        setAccessToken(state, payload){
            state.accessToken = payload.token;
        },
        setPortfolios(state, payload){
            state.portfolios = payload.portfolios;
        },
        setPosts(state, payload){
            state.posts = payload.posts;
		},
		setUsers(state, payload) {
			state.users = payload.users;
		},
		setCounts(state, payload){
			state.counts = payload.counts;
        }
    },
    getters:{
        getSource: function(state){
            return state.source;
        },
        getTarget: function(state){
            return state.target;
        },
        getUser : function(state){
            return state.user;
        },
        getAccessToken : function(state){
            return state.accessToken;
        },
        getPortfolios : function(state){
            return state.portfolios;
        },
        getPosts : function(state){
            return state.posts;
        },
        getImagebannersrc : function(state){
            return state.imagebannersrc;
		},
		getUsers : function(state) {
			return state.users;
		},
		getCounts : function(state){
			return state.counts;
        }
	},
    plugins: [new VuexPersistence({
        storage: window.sessionStorage,
        reducer: (state) => ({user: state.user}),	// 새로고침시 붙잡아 주는 코드
    }).plugin]
})
