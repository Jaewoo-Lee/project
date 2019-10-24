<template>
    <v-layout mt-5 style="max-width:100%">
        <v-flex xs12>
            <v-card flat color="transparent">
            <v-card-title>
                <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="search"
                    label="Search"
                    single-line
                    hide-details
                >
				</v-text-field>
            </v-card-title>
            <v-card-text>
            <v-data-table
                :headers="headers"
                :items="members"
                :search="search"
                item-key="userId"
                class="elevation-5"
                style="margin:0px 0px;"
                >
                <template v-slot:items="props" style="width:100%">
                    <tr :active="!!selected && selected.userId == props.item.userId && props.item.authority != 'ADMIN'"
                        @click="selected = props.item">
                        <td class="text-xs-left">{{ props.item.userId }}</td>
                        <td class="text-xs-left">{{ props.item.authority }}</td>
                    </tr>
                </template>
            </v-data-table>

            <v-btn dark color="primary" @click.stop="dialog = true" :disabled="selected.length==0 || selected.authority=='ADMIN'">
                Confirm
            </v-btn>
            </v-card-text>
        </v-card>
        </v-flex>
        <v-dialog v-model="dialog" :width="$vuetify.breakpoint.xs ? 300 : 600 " scrollable>
            <v-card>
                <v-card-title class="headline font-weight-bold" primary-title>selected</v-card-title>
                <v-card-text class="font-weight-light title">
                        {{selected.userId}}
                </v-card-text>
                <v-card-actions>
                    <v-select :items="levels" label="Level" v-model="selectedLevel"></v-select>
                    <v-spacer></v-spacer>
                    <v-btn small text @click="dialog=false">
                        Cancel
                    </v-btn>
                    <v-btn color="primary" small text @click="confirm" :disabled="selectedLevel==''">
                        Confirm
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-layout>
</template>


<script>
import controller from '@/services/Controller'

export default {
    name: 'AdminMember',
    data() {
        return {
            dialog: false,
            search: '',
            selected: {authority : 'ADMIN'},
            headers : [
                {
                    text: 'ID',
                    sortable: false,
                    value: 'userId',
                },
                { text: 'Level', value: 'authority' },
            ],
            members : [],
            levels : [
                'MEMBER',
                'VISITOR'
            ],
            selectedLevel : ''
        };
    },
    methods : {
        async searchAuthorities(){
            try{
                await controller.searchAuthorities();
            } catch(e){
                alert(e)
            }
        },
        async changeAuthority(){
            try{
                await controller.changeAuthority(this.selected.userId, this.selectedLevel);
            } catch(e){
                alert(e)
            }
        },
        confirm(){
            this.changeAuthority();
            this.dialog = false;
        }
    },
    mounted(){
        this.searchAuthorities();
    },
    computed:{
        watchUsers(){
            return this.$store.getters.getUsers;
        }
    },
    watch:{
        'dialog' : function(value, oldValue) {
            if(!value){
                this.selected = [];
                this.selectedLevel = '';
            }
        },
        watchUsers(val,oldVal){
            this.members = val;
        }
    },
}
</script>

<style scoped>
table{
display: inline-block;
margin : 0px 0px;
}
</style>
