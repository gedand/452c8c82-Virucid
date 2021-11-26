function contentsLoad()
{
    var url=window.location.href
    let paramString = url.split('?')[1];
    let queryString = new URLSearchParams(paramString);
    
    for (let pair of queryString.entries()) {
    sessionStorage.setItem(pair[0],pair[1]);
    }
    var mainImage=document.getElementById('mainImage');
    var imageId=sessionStorage.getItem('imageId');
    mainImage.src=imageId;

}
function commentUploadPost()
{
    var url = "http://localhost:5000/comment";
    var formData = new FormData();
    var fileId=sessionStorage.getItem('imageId');
    comment=document.getElementById('commentInput').value;

    formData.append("comment", comment);
    formData.append("fileId", fileId); 

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);
    var token=sessionStorage.getItem('token')
    
    xhr.setRequestHeader("Authorization", "Bearer "+token );
    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        const responseObj = JSON.parse(xhr.responseText);
      if(xhr.status==200)
      {
        picturesShow(responseObj)
      }
     

    }};

    xhr.send(formData);
}