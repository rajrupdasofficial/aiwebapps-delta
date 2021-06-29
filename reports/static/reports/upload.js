const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].Value

Dropzone.autoDiscover=false

const myDropzone = new Dropzone ('#my-dropzone',{
    url:'/reports/upload/',
    init:function(){
        this.on('sending',function(file,xhr,formData){
            console.log('sending')
            formData.append('csrfmiddlewaretoken',csrf)
        })
    },
    maxFiles:3,
    maxFilesize:50,
    acceptedFiles:'.csv'
})