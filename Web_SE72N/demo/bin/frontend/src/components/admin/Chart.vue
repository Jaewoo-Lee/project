<script>
import {Line, mixins} from 'vue-chartjs'	// Importing Line class from the vue-chartjs
import controller from '@/services/controller'

export default {
	extends: Line,
	props: ['options', 'data'],
	mounted () {
		this.renderChart(this.data,this.options)
	},
}
</script>
