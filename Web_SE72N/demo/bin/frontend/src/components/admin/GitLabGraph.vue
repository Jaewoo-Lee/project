<template>
    <v-layout align-center px-4 column>
        <hooper style="height:100%;">
            <slide v-for="(user,i) in users" :key="i">
                <v-card class="mx-auto text-center" width="600">
                    <v-card-title>
                        {{user.name}}
                    </v-card-title>
                    <v-card-text>
                        <v-sheet color="rgba(0, 0, 0, .12)">
                            <my-chart v-if="finished" :data="chartData[i]" :options="options"/>
                        </v-sheet>
                    </v-card-text>
                </v-card>
            </slide>
            <hooper-pagination slot="hooper-addons" mode="fraction"></hooper-pagination>
        </hooper>
    </v-layout>
</template>


<script>
import MyChart from '@/components/admin/Chart'
import { Line } from 'vue-chartjs'
import axios from 'axios'
import VueCharts from 'vue-chartjs'
import { Hooper, Slide,  Pagination as HooperPagination } from 'hooper';

export default {
    name: 'GitLabGraph',
    extends:Line,
    components: {
        MyChart,
        Hooper,
        Slide,
        HooperPagination
    },
    data() {
        return {
            users : [
                {userId : 148, token : '7Z_hPJyASsAHczS7ats-', name : "김동환"},
                {userId : 334, token : 'QGxKcg8Yj3xYDy9uoou-', name : "김유나"},
                {userId : 529, token : 'zyzfqCVsGqz8RytZLWbt', name : "양희동"},
                {userId : 106, token : 'k2fAvDUNQxiUATLQpNTA', name : "이민영"},
                {userId : 195, token : 'z1ZjboLopHW2_Vp3Hivf', name : "이재우"},
            ],
            labels: [
                '07-22', '07-23', '07-24', '07-25',
                '07-26', '07-27', '07-28', '07-29',
                '07-30', '07-31', '08-01', '08-02',
                '08-03', '08-04', '08-05', '08-06',
                '08-07', '08-08', '08-09', '08-10',
                '08-11', '08-12', '08-13', '08-14',
            ],
            datasets: [
                {
                    label: 'number of commits per day',
                    backgroundColor: 'white',
                    pointBackgroundColor: 'white',
                    borderWidth: 1,
                    pointBorderColor: '#249EBF',
                    data:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                },
                {
                    label: 'number of commits per day',
                    backgroundColor: 'white',
                    pointBackgroundColor: 'white',
                    borderWidth: 1,
                    pointBorderColor: '#249EBF',
                    data:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                },
                {
                    label: 'number of commits per day',
                    backgroundColor: 'white',
                    pointBackgroundColor: 'white',
                    borderWidth: 1,
                    pointBorderColor: '#249EBF',
                    data:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                },
                {
                    label: 'number of commits per day',
                    backgroundColor: 'white',
                    pointBackgroundColor: 'white',
                    borderWidth: 1,
                    pointBorderColor: '#249EBF',
                    data:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                },
                {
                    label: 'number of commits per day',
                    backgroundColor: 'white',
                    pointBackgroundColor: 'white',
                    borderWidth: 1,
                    pointBorderColor: '#249EBF',
                    data:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                }
            ],
            options: {	// 차트의 모양을 제어하는 ​​Chart.js 옵션
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        },
                        gridLines: {
                            display: true
                        }
                    }],
                    xAxes: [ {
                        gridLines: {
                            display: false
                        }
                    }]
                },
                legend: {
                    display: true
                },
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 0
                },
                hover: {
                    animationDuration: 0
                },
                responsiveAnimationDuration: 0
            },
            chartData : [
                {
                    labels: [],
                    datasets:[]
                },
                {
                    labels: [],
                    datasets:[]
                },
                {
                    labels: [],
                    datasets:[]
                },
                {
                    labels: [],
                    datasets:[]
                },
                {
                    labels: [],
                    datasets:[]
                }
            ],
            finished:false
        }
    },
    methods:{
        getEvents(userId, token, i){
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
                    var d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
                    res.data.forEach(function(item){
                        this.labels.some(function(val, j){
                            if(item.created_at.includes(val)){
                                d[j]++;
                                return true;
                            }
                        }, this)
                    }, this)
                    this.datasets[i].data = d;
                    this.chartData[i].labels=this.labels;
                    this.chartData[i].datasets[0]=this.datasets[i];
                    resolve(res.data)
                })
                .catch(err => {
                    console.log("err : " + err)
                })
            });
        },
        async setData(i){
            for(var i=0; i<this.users.length; i++){
                await this.getEvents(this.users[i].userId, this.users[i].token, i)
            }
            this.finished=true;
        },
    },
    mounted(){
        this.setData();
    },
}
</script>
