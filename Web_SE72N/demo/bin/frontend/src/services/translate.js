import axios from 'axios'
import store from '../store'

export default{
    translate(input){
        input += ''
        return new Promise((resolve, reject) => {
            let url = 'https://www.googleapis.com/language/translate/v2';
            axios.post(url, null, {
                params :{
                    key : "AIzaSyB1MlJJ6B0QaVmOWHp8YjACHAjub-VF8_Q",
                    source : store.state.source,
                    target : store.state.target,
                    q : input
                }
            })
            .then(response => {
                //console.log(response.data.data.translations[0].translatedText)
                resolve(response.data.data.translations[0].translatedText)
            })
            .catch(e => {
                alert("error" + e)
            })
        });
    }
}
