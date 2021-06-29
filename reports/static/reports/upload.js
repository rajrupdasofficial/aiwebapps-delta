const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].Value
const  alertBox=document.getElementById("alert-box")

const handleAlerts=(type,msg)=>{
    alertBox.innerHTML=`
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}



Dropzone.autoDiscover=false

const myDropzone = new Dropzone ('#my-dropzone',{
    url:'/reports/upload/',
    init:function(){
        this.on('sending',function(file,xhr,formData){
            console.log('sending')
            formData.append('csrfmiddlewaretoken',csrf)
        })
        this.on('success',function(file,response){
            console.log(response)
            const ex=response.ex
            if(ex){
                handelAlerts('danger',"File Already Exists")
            }else{
              handelAlerts('success',"File has uploaded")
            }
        })
    },
    maxFiles:3,
    maxFilesize:50,
    acceptedFiles:'.csv'
})