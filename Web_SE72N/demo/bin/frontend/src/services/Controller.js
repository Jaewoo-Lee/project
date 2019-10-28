import axios from 'axios'
import router from '@/router/index'
import store from '@/store'
import Api from '@/services/Api'

const url = 'http://70.12.247.54:8080/'

export default{
	// 페이지 로그 저장
	saveLog(pageName){
		return new Promise((resolve, reject) => {
			axios
				.post(url + 'log.do', {
					userId : store.getters.getUser.id,
					pageName : pageName
				})
				.then(res => {
					resolve(res.data)
				})
				.catch(e => {
					console.log(e)
				})
		})
	},

	// 로그 리스트 조회
	getLogs(){
        return new Promise((resolve, reject) => {
			axios
				.get(url + 'getLog.do')
				.then(res => {
					resolve(res.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
        });
	},

	// 포트폴리오 리스트 조회
	getPortfolios(){
        return new Promise((resolve, reject) => {
			axios
				.get(url + 'searchAllPortfolio.do')
				.then(response => {
					store.commit('setPortfolios', {portfolios : response.data})
					resolve(response.data)
				})
				.catch(e => {
					console.log("err : " + e)
				})
        });
	},

	// 포트폴리오 글 작성 및 수정
	savePortfolio(num, title, content, image){
		return new Promise((resolve, reject) => {
			axios
				.post(url + 'newPortfolio.do', {
					portNum : num,
					portTitle : title,
					portContent : content,
					portImg : image,
					userId : store.getters.getUser.id
				})
				.then(response => {
					store.commit('setPortfolios', {portfolios : response.data})
					router.push({name: 'portfolio'})
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
		});
	},

	// 포트폴리오 글 삭제
	deletePortfolio(num){
        return new Promise((resolve, reject) => {
			axios
				.delete(url + 'deletePortfolio.do', {
					params:{
						portNum : num
					}
				})
				.then(response => {
					store.commit('setPortfolios', {portfolios : response.data})
					router.push({name: 'portfolio'})
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
        });
	},

	// 포트폴리오 댓글 작성 및 수정
	savePortfolioComment(payload){
        return new Promise((resolve, reject) => {
			axios
				.post(url + 'writePortfolioComment.do', {
					portcommentNum : payload.portcommentNum,
					portNum : payload.portNum,
					userId : payload.userId,
					portcommentContent : payload.portcommentContent
				})
				.then(response => {
					store.commit('setPortfolios', {portfolios : response.data})
					console.log(response.data)
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
        });
	},

	// 포트폴리오 댓글 삭제
	deletePortfolioComment(num){
        return new Promise((resolve, reject) => {
			axios
				.delete(url + 'deletePortfolioComment.do', {
					params:{
						portcommentNum : num
					}
				})
				.then(response => {
					store.commit('setPortfolios', {portfolios : response.data})
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
        });
	},

	// 포스트 리스트 조회
	getPosts(){
        return new Promise((resolve, reject) => {
			axios
				.get(url + 'searchAllPost.do')
				.then(response => {
					store.commit('setPosts', {posts : response.data})
					resolve(response.data)
				})
				.catch(e => {
					console.log("err : " + e)
				})
        });
	},

	// 포스트 글 작성 및 수정
	savePost(num, title, content){
		return new Promise((resolve, reject) => {
			axios
				.post(url + 'newPost.do', {
					postNum : num,
					postTitle : title,
					postContent : content,
					userId : store.getters.getUser.id
				})
				.then(response => {
					store.commit('setPosts', {posts : response.data})
					router.push({name: 'post'})
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
		});
	},

	// 포스트 글 삭제
	deletePost(num){
        return new Promise((resolve, reject) => {
			axios
				.delete(url + 'deletePost.do', {
					params:{
						postNum : num
					}
				})
				.then(response => {
					store.commit('setPosts', {posts : response.data})
					router.push({name: 'post'})
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
        });
	},

	// 포스트 댓글 작성 및 수정
	savePostComment(payload){
        return new Promise((resolve, reject) => {
			axios
				.post(url + 'writePostComment.do', {
					postcommentNum : payload.postcommentNum,
					postNum : payload.postNum,
					userId : payload.userId,
					postcommentContent : payload.postcommentContent
				})
				.then(response => {
					store.commit('setPosts', {posts : response.data})
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
        });
	},

	// 포스트 댓글 삭제
	deletePostComment(num){
        return new Promise((resolve, reject) => {
			axios
				.delete(url + 'deletePostComment.do', {
					params:{
						postcommentNum : num
					}
				})
				.then(response => {
					store.commit('setPosts', {posts : response.data})
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
        });
	},

	// 로그인 확인
	login(id, pw){
        return new Promise((resolve, reject) => {
			axios
				.post(url + 'login.do', {
					userId : id,
					userPass : pw
				})
				.then(response => {
					resolve(response.data)
				})
				.catch(e => {
					console.log("err" + e)
				})
        });
	},

	// 회원가입
	register(id, pw, gitId){
      return new Promise((resolve, reject) => {
		axios
			.post(url + 'addUser.do', {
				userId : id,
				userPass : pw,
				githubId : gitId
			})
			.then(response => {
				resolve(response.data)
			})
			.catch(e => {
				console.log("err" + e)
			})
      });
	},

	// 유저의 권한 리스트 조회
	searchAuthorities() {
		return new Promise((resolve, reject) => {
			axios
				.get(url + 'searchAuthorities.do')
				.then(response => {
					store.commit('setUsers', {users : response.data})
					resolve(response.data)
				})
				.catch(e => {
					console.log("err : " + e)
				})
		});
	},

	// 유저의 권한 변경 ( 관리자만 )
	changeAuthority(userId, authority) {
		return new Promise((resolve, reject) => {
			axios
				.post(url + 'changeAuthority.do', {
					userId : userId,
					authority : authority
				})
				.then(response => {
					store.commit('setUsers', {users : response.data})
					resolve(response.data)
				})
				.catch(e => {
					console.log("err : " + e)
				})
		});
	},


	// gitlab 서비스
	getEvents(userId, token){
		return new Promise((resolve, reject) => {
			axios
			.get(`https://lab.ssafy.com/api/v4/users/${userId}/events`,{
				params:{
					after : '2019-07-21',
					before : '2019-08-16',
					private_token : token,
					action : 'pushed',
					per_page : 200
				}
			})
			.then(res => {
				resolve(res.data)
			})
			.catch(err => {
				console.log("err : " + err)
			})
		});
	},
	// 토큰 저장하기
	saveToken(token) {
		return new Promise((resolve, reject) => {
			axios
				.post(url + 'saveToken.do', {
					tokenInfo : token
				})
				.then(response => {
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
		})
	},

	// 토큰 조회
	findToken() {
		return new Promise((resolve, reject) => {
			axios
				.get(url + 'findToken.do')
				.then(response => {
					resolve(response.data)
				})
				.catch(err => {
					console.log("err : " + err)
				})
		})
	},

	// 푸쉬 알림 보내기(글 작성, 수정, 댓글 작성, 수정)
	sendNotification(list, title, body) {
		return new Promise((resolve, reject) => {
			axios
				.post('http://fcm.googleapis.com/fcm/send', {
					"notification" : {
						"body": body,
						"title" : title,
						"click_action" : 'https://www.google.com',
						"data" : {
							"click_action" : 'https://www.naver.com'
						}
					},
					"registration_ids" : list
					}, {
						headers : {
							"Content-Type": 'application/json',
							"Authorization": 'key=AAAAF0e2OfI:APA91bGfT-wZppDqnx55JW9rAiE8jhU1QbytJp2FYpDMkBo5FZs3WqFTRHX2DqY6ve-jir0aR9sjuD4ty1lwO9sYf1NehCmtNGlkbiAFSPQkPJSam3hvFTo4nwdqfIt43XcMWQ_Hnhv_'
						}
					}
				)
				.then(response => {
					console.log(response)
					resolve(response)
				})
				.catch(err => {
					console.log(err)
				})
		})

	}

}
