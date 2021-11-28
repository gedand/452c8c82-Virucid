var extension=".jpg";
var extensionCaff=".caff"
var urlStart="http://localhost:5000/download/";
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
    mainImage.src=urlStart+imageId+extension;

    commentFetch();

}
function commentUploadPost()
{
    var url = "http://localhost:5000/comment";
    var formData = new FormData();
    var filename=sessionStorage.getItem('imageId');
    comment=document.getElementById('commentInput').value;

    formData.append("comment", comment);
    formData.append("filename", filename); 

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

function commentUploadPost1()
{
    var url = "http://localhost:5000/comment";
    var formData = new FormData();
    var fileId=sessionStorage.getItem('imageId');
    comment=document.getElementById('commentInput').value;

    formData.append("comment", comment);
    formData.append("file_id", "xewd8pdp3tc53j86"); 

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
function commentFetch()
{
    var url = "http://localhost:5000/comment";
    var formData = new FormData();
    var filename=sessionStorage.getItem('imageId');

    formData.append("filename", filename); 

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);
    var token=sessionStorage.getItem('token')
    
    xhr.setRequestHeader("Authorization", "Bearer "+token );
    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        const responseObj = JSON.parse(xhr.responseText);
      if(xhr.status==200)
      {
        generateComments(responseObj)
      }
     

    }};

    xhr.send(formData);
}
function generateComments(data)
{
  //data=["見えないとこでバタ足するんです","見えないとこでバタ足するんです","見えないとこでバタ足するんです"];
  var div=document.getElementById('commentDiv');
  for(i=0; i<=Object.keys(data.comments).length-1;i++)
    {
  var containerDiv=document.createElement('div');
  containerDiv.className='mt-4 text-justify float-left';
  var commentP=document.createElement('p')
  var text =data.comments[i]
  commentP.append(text);
  containerDiv.appendChild(commentP);
  div.appendChild(containerDiv);
  
  } 
  



}
function deleteImagePost()
{
  var url = "http://localhost:5000/delete";
  var formData = new FormData();
  var fileId=sessionStorage.getItem('imageId');

  formData.append("filename", fileId); 

  var xhr = new XMLHttpRequest();
  xhr.open("POST", url);
  var token=sessionStorage.getItem('token')
  
  xhr.setRequestHeader("Authorization", "Bearer "+token );
  xhr.onreadystatechange = function () {
  if (xhr.readyState === 4) {
      const responseObj = JSON.parse(xhr.responseText);
    if(xhr.status==200)
    {
      window.location.href = 'index.html';
    }
   

  }};

  xhr.send(formData);


}
function downloadImagePNG()
{
  var source=urlStart+sessionStorage.getItem('imageId')+extension;
  const fileName = source.split('/').pop();
	var el = document.createElement("a");
	el.setAttribute("href", source);
	el.setAttribute("download", fileName);
	document.body.appendChild(el);
 	el.click();
	el.remove();


}
function downloadImageCaff()
{
  
  var source=urlStart+sessionStorage.getItem('imageId')+extensionCaff;
  const fileName = source.split('/').pop();
	var el = document.createElement("a");
	el.setAttribute("href", source);
	el.setAttribute("download", fileName);
	document.body.appendChild(el);
 	el.click();
	el.remove();


}


