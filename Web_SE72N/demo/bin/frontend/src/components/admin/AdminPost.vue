<template>
	<v-layout mt-5 wrap>
		<v-flex pa-2 xs12 sm6>
			<v-card>
				<v-card-text>
					<v-data-table
					:headers="headers"
					:items="items"
					item-key="type"
					hide-actions
					>
						<template slot="items" scope="props">
							<td class="text-xs-left">{{ props.item.type }}</td>
							<td class="text-xs-left">{{ props.item.value }}</td>
						</template>
					</v-data-table>
				</v-card-text>
			</v-card>
		</v-flex>
		<v-flex pa-2 xs12 sm6>
			</v-card>
		</v-flex>
	</v-layout>
</template>


<script>
import controller from '@/services/Controller'

export default {
	name: 'AdminPost',
	data() {
		return {
			headers : [
				{ text: 'Category', align: 'left', sortable: false, value: 'category' },
				{ text: 'number of', value: 'value' }
			],
			items : [
				{ type: 'portfolios', value: 0},
				{ type: 'posts', value: 0}
			],
		};
	},
	methods : {
		countList(){
			this.items[0].value =  this.$store.getters.getPortfolios.length;
			this.items[1].value =  this.$store.getters.getPosts.length;
		}
	},
	mounted(){
		this.countList();
	},
	computed:{
		watchPortfolios(){
            return this.$store.getters.getPortfolios.length;
        },
		watchPosts(){
            return this.$store.getters.getPosts.length;
        }
	},
	watch:{
		watchhPortfolios(val,oldVal){
            this.items[0].value = val;
        },
		watchPosts(val,oldVal){
            this.items[1].value = val;
		}
	},
}
</script>
