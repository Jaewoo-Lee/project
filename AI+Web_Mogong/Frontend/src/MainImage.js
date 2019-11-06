import React ,{ Component } from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';

class MainImage extends Component {
  constructor(props){
    super(props);
    this.state = {
      charPoses : {
        exit: { y: 20, opacity: 0 },
        enter: {
          y: 0,
          opacity: 1,
          transition: ({ charInWordIndex }) => ({
            type: 'spring',
            delay: charInWordIndex * 30,
            stiffness: 500 + charInWordIndex * 150,
            damping: 10 - charInWordIndex * 1
          })
        }
      },
      image : '',
      afterUrl : '',
      changeimage : '',
      file : null,
      selectedFile: null,
    }
  }
  uploadImage(){
    const formData = new FormData()
    const file = document.getElementById('ex_file').files[0]
    if(file==null){
      alert("이미지를 선택해 주세요.")
    }
    else{
      formData.append("image",file)
      axios({
        method : "POST",
        url : "https://api.imgur.com/3/image",
        timeout: 0,
        headers: {
          "Authorization": "Client-ID acd50197869043a",
        },
        processData: false,
        mimeType: "multipart/form-data",
        contentType: false,
        data: formData
      })
      .then(res=> {
        this.setState({
          image : res.data.data.link,
        });
        axios({
          url : "/upload.do?url="+this.state.image,
          headers : {
            "Access-Control-Allow-Origin" : "*",
          },
          data : this.state.image,
        })
        .then(response=>{
          console.log("이미지 보내기 완료.")
          this.setState({
            afterUrl : response.data
          });
        })
        .catch( error=>{
          console.log('실패',error)
        })
        
      })
      
    }
    }
    resetInput(){
      document.getElementsById('ex_file').reset();
    }
    render(){
    return(
      <div>
        <div style={{width:"100%", textAlign:"center"}}>
          <div style={{display:"inline-block"}}>
            <img src={this.state.image} alt="" style={{width:"300px",height:"auto" , marginRight:"10px"}}></img>
            <img src={this.state.afterUrl} alt="" style={{width:"300px",height:"auto"}}></img>
          </div>
        </div>
        <br/>
        <div style={{margin:"auto"}}>
            <div>
            <input
              accept="image/*"
              style={{ display: 'none' }}
              id="ex_file"
              multiple
              type="file"
              onChange={()=>this.uploadImage()}
            />
            <label htmlFor="ex_file">
              <Button variant="contained" component="div" color="primary">
                Upload Image
              </Button>
            </label> 
            </div>
        </div>
      </div>
    );
  }
} 
export default MainImage;