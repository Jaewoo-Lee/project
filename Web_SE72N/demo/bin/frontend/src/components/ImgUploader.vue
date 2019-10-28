<template>
	<div>
		<v-layout>
			<v-flex xs12>
				<v-card>
					<img id="image" class="white--text" height="100%" width="100%" :src="imgSrc">
					<v-card-actions>
						<v-layout row justify-center>
							<div class="filebox">
								<v-btn class="p-0" color="rgba(182, 198, 207, 1)" dark v-on:click="getRandomImg">RANDOM</v-btn>
								
								<!-- 파일첨부를 하면 바로 서버에 전송을 하게 되고 추가 버튼을 누르면 그 이미지링크를 마크다운에디터에 띄워준다. -->
								<v-btn class="p-0" color="rgba(182, 198, 207, 1)" dark>
									<label for="fileupload1">파일첨부</label>
								</v-btn>
								<input multiple accept="image/*" id="fileupload1" name="file1" ref="file1" type="file" v-on:change="Thumbnail"/>>
								<v-btn class="p-0 mx-2" color="rgba(182, 198, 207, 1)" dark v-on:click="ImgUpload">추가하기</v-btn>
							</div>
						</v-layout>
					</v-card-actions>
				</v-card>
			</v-flex>
		</v-layout>
	</div>
</template>

<script>
export default {
	name: 'ImgUploader',
	props:{
		parentMessage : { type : String }
	},
	data() {
		return {
			file:'',
			imgSrc:this.getImgUrl('noimage2.png'),
			childMessage:''
		}
	},
	methods: {
		getImgUrl(imgsrc) {
			return require('../assets/' + imgsrc)
		},
		Thumbnail(){
			var image = document.getElementById('image');
			this.file = this.$refs.file1.files[0];
			var reader = new FileReader();

			reader.readAsDataURL(this.file)
			reader.onload = function(e){
				image.src = e.target.result;
			}
		},
		getRandomImg(){
			var image = document.getElementById('image');
			const BASE_URL = 'https://source.unsplash.com/random/1600x900'
			this.$http
				.get(`${BASE_URL}`)
				.then((result) => {
					if (result.status == 200){
						image.src = result.request.responseURL
						this.imgSrc = result.request.responseURL
					}
				})
		},
		ImgUpload() {
			const BASE_URL = 'https://api.imgur.com/3/image.json'
			const formData = new FormData();
			var image = document.getElementById('image');
			this.file = this.$refs.file1.files[0];
			if(this.file){
				formData.append('image',this.file);
			} else{
				formData.append('image',this.imgSrc);
			}
			this.$http
				.post(`${BASE_URL}`,formData, {
					'headers':{'Authorization':'Client-ID 7126f20a233f2ae',}
				})
				.then((result) => {
					if (result.status == 200) {
						this.childMessage = " ![]("+`${result.data.data.link}`+")"
						this.$emit('send-message',this.childMessage)
						image.src = result.data.data.link
					} else{
						alert("업로드 실패");
						image.src = "http://dy.gnch.or.kr/img/no-image.jpg";
					}
				})
		}
	}
}
</script>

<style scoped>
.mx-auto {
	margin-left: auto;
	margin-right:auto;
}

.wd-100 {
	width:100%;
}

.ml-auto {
	margin-left:auto;
}

.footer-color {
	background: linear-gradient(
		to right,
		#e730c9,
		#f34865
	);
}

.mx-2 {
	margin-left: 2px;
	margin-right:2px;
}

.p-0 {
	padding:0px;
	text-decoration-color: white;
}

footer {
	position: relative;
	bottom: 0;
	width: 100%;
	padding: 0px 20px;
	height: 80px;
	text-align: left;
	font-size:0.7em;
	box-sizing: border-box;
	background: -webkit-linear-gradient(
		to right,
		#e730c9,
		#f34865
	);
	background: linear-gradient(
		to right,
		#e730c9,
		#f34865
	);
	z-index:4;
}

.filebox label {
	display: inline-block;
	padding: .6em 1.13em;
	color: white;
	font-size: inherit;
	line-height: normal;
	vertical-align: middle;
	cursor: pointer;
}

/* 파일 필드 숨기기 */
.filebox input[type="file"] {
	position: absolute;
	width: 1px;
	height: 1px;
	padding: 0;
	margin: -1px;
	overflow: hidden;
	clip:rect(0,0,0,0);
	border: 0;
}

</style>
