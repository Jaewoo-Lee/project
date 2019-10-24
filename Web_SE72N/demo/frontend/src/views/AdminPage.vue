<template>
    <v-container>
        <v-layout justify-center fill-height elevation-5 style="min-height:500px;" pa-4>
            <v-flex xs12 text-xs-center>
                <v-tabs dark color="blue darken-1">
                    <v-tabs-slider color="yellow accent-4"></v-tabs-slider>
                    <v-tab v-for="(item, i) in tabs" :key="i" :href="'#tab-' + i">
                        {{item}}
                    </v-tab>

                    <v-tabs-items>
                        <v-tab-item v-for="(item,i) in tabs" :key="i" :value="'tab-' + i">
                            <template v-if="i==0">
                                <template v-if="!$vuetify.breakpoint.xs">
                                    <graph />
                                </template>
                                <template v-else>
                                    <div>현재 디바이스에선 확인할 수 없습니다.</div>
                                </template>
                            </template>
                            <template v-else-if="i==1">
                                <member/>
                            </template>
                            <template v-else-if="i==2">
                                <post/>
                            </template>
                        </v-tab-item>
                    </v-tabs-items>
                </v-tabs>

                <v-btn color="green accent-4" fab dark small absolute top right style="margin-top:50px" @click.stop="dialog=true">
                    <v-icon>home</v-icon>
                </v-btn>

            </v-flex>

            <v-dialog v-model="dialog" :width="$vuetify.breakpoint.xs ? 300 : 600 " scrollable>
                <v-card>
                    <v-card-title class="headline font-weight-bold" primary-title>back to home</v-card-title>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn small text @click="dialog=false">
                            Cancel
                        </v-btn>
                        <v-btn color="primary" small text @click="gotohome">
                            Go
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-layout>
    </v-container>
</template>


<script>
import member from '@/components/admin/AdminMember'
import post from '@/components/admin/AdminPost'
import graph from '@/components/admin/GitLabGraph'
import router from '@/router/index'

export default {
    name: 'AdminPage',
    data() {
        return {
            tabs : [
                'Team',
                'Member',
                'Post'
            ],
            dialog : false,
        }
    },
    components : {
        member,
        post,
        graph
    },
    computed:{
        watchUser(){
            return this.$store.getters.getUser;
        }
    },
    watch:{
        watchUser(val,oldVal){
            console.log(val)
            if(val.level != 'ADMIN'){
                alert("비정상적인 접근입니다.")
                this.$router.push({name : 'home'})
            }
        }
    },
    methods:{
        gotohome(){
			setTimeout(function() {
				router.push({name: 'home'})
			}, 600);
		},
    }
}
</script>
