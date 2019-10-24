<template>
    <v-layout row justify-center>
        <!-- 현재 로그아웃 상태라면 로그인 버튼, 로그인 상태라면 로그아웃 버튼 노출 -->
        <v-btn class="login_btn" flat @click.stop="showLogin=true" v-if="user.level=='GUEST'">Login</v-btn>
        <v-btn class="login_btn" flat @click="logout" v-else>Logout</v-btn>

        <v-dialog v-model="showLogin" width="300">
            <v-card>
                <v-card-title><h3 style="text-align: center; width:100%; text-decoration: bold;">Login</h3></v-card-title>
                <v-card-text>
                    <form v-on:submit.prevent="sendPost">
                        <div class="modal">
                            <input v-model="id" placeholder="ID" style="width:90%"  type="email"    @keyup.enter="enter">
                            <input v-model="pw" placeholder="PW" style="width:90%"  type="password" @keyup.enter="enter">
                        </div>

                        <v-layout class="modal" column align-center>
                            <v-btn flat :disabled="can" @click="sendPost" style="width:50%">
                                Login
                            </v-btn>
                            <v-btn depressed color='#1976D2' dark @click="loginWithFacebook" style="width:50%">
                                Facebook Login
                            </v-btn>
                            <v-btn flat @click="showReg=true;showLogin=false;" style="width:50%">
                                Register
                            </v-btn>
                        </v-layout>
                    </form>
                </v-card-text>
            </v-card>
        </v-dialog>
        <!-- 회원가입 -->
        <v-dialog v-model="showReg" width="300">
            <v-card>
                <v-card-title><h3 style="text-align: center; width:100%; text-decoration: bold;">Join</h3></v-card-title>
                <v-card-text>
                    <form v-on:submit.prevent="sendPostReg">
                        <div>
                            <input v-model="idreg" placeholder="ID" id="email" style="width:90%">
                            <input v-model="pwreg" placeholder="PW" type="password" style="width:90%">
                            <input v-model="pwchk" placeholder="PW check" type="password" style="width:90%">
                            <input v-model="github" placeholder="Github ID" style="width:90%">
                        </div>

                        <v-layout class="modal" column align-center style="width:50%">
                            <v-btn flat @click="sendPostReg" :disabled="canReg">
                                Register
                            </v-btn>
                        </v-layout>
                    </form>
                </v-card-text>
            </v-card>
        </v-dialog>

    </v-layout>
</template>


<script>
import FirebaseService from "@/services/FirebaseService"
import controller from "@/services/Controller"

export default{
    data() {
        return{
            fab: false,
            id : '',
            pw : '',
            idreg : '',
            pwreg : '',
            pwchk : '',
            github : '',
            showLogin : false,
            showReg : false,
            user : {
                id : '',
                level : 'GUEST',
            }
        }
    },
    methods: {
        sendPost: async function () {
            const exptext = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
            //이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우
            if(exptext.test(this.id)==false){
                alert("아이디는 이메일 형식으로 입력하세요!");
                return;
            }
            try{
                var res = await controller.login(this.id,this.pw);
                console.log(res);
                if(res.authority !== 'GUEST'){
                    this.hide();
                    this.login(res);
                    this.id = '';
                }
                else{
                    alert("일치하는 회원정보가 없습니다.")
                }
                this.pw = '';
            } catch(e){
                alert(e)
            }
        },
        sendPostReg: async function () {
            const exptext = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
            //이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우
            if(exptext.test(this.idreg)==false){
                alert("아이디는 이메일 형식으로 입력하세요!");
                return;
            }
            if(this.pwreg != this.pwchk){
                alert("비밀번호가 서로 다릅니다.")
                return;
            }
            var res = await controller.register(this.idreg, this.pwreg, this.github);
            if(res){
                alert("회원가입 성공")
                this.showLogin = true;
                this.showReg = false;
                await controller.searchAuthorities();
            }
            else{
                alert("회원가입 실패")
            }
            this.idreg = '';
            this.pwreg = '';
            this.pwchk = '';
            this.github = '';
        },
        hide(){
            this.showLogin=false;
            this.showReg=false;
            this.idreg = '';
            this.pwreg = '';
            this.pwchk = '';
            this.github = '';
            this.id = '';
            this.pw = '';
        },
        logout(){
            if (this.$store.getters.getAccessToken !== '') {
                this.logoutFacebook()
            }
            this.$store.commit('logout')
        },
        login(user){
            this.$store.commit('login',{id : user.userId, authority : user.authority, github: user.githubId});
            console.log('login')
            console.log(this.user)
        },
        enter(){
            if(this.id!='' && this.pw!=''){
                this.sendPost();
            }
        },
        async loginWithFacebook(){
            try {
                const result = await FirebaseService.loginWithFacebook()
                const email = result.user.email
                this.$store.commit('setAccessToken',{token : result.credential.accessToken})
                this.$store.commit('login',{id : email, level : 'VISITOR'})
                this.showLogin = false
                this.hide()
                alert('페이스북 로그인 되었습니다.')
            }
            catch(error) {
                alert('페이스북 이메일 또는 비밀번호를 확인해주세요.')
            }
        },
        async logoutFacebook() {
            try {
                await FirebaseService.logoutFacebook()
                alert('페이스북 로그아웃 되었습니다.')
            }
            catch(error) {
                alert('로그아웃 실패')
            }
        }
    },
    computed:{
        can(){
            if(this.id == '' || this.pw == '')
            return true;
            return false;
        },
        canReg(){
            if(this.idreg=='' || this.pwreg=='' || this.pwchk=='' || this.github=='')
            return true;
            return false;
        },
        isLogin(){
            return this.$store.getters.getUser;
        },
    },
    mounted(){
        this.user = this.$store.getters.getUser;
    },
    watch:{
        isLogin(val, oldVal){
            this.user = val;
        }
    }
}
</script>


<style scoped>
.header{
    margin:auto;
}
.modal{
    text-align: center;
    margin:auto;
}
</style>
