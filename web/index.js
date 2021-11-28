
var array1=[1,1,2];
var extension=".jpg";
function picturesShow(array)
{
  array1=array;
  var arr=["assets/images/work-2.jpg","assets/images/work-2.jpg","assets/images/work-2.jpg"];

    //var arr=['omae','mo','shindeiru'];
    var ul=document.getElementById('works-grid');
    removeAllChildNodes(ul);
    var url="http://localhost:5000/download/";
    

    for(i=1; i<=Object.keys(array.files).length-1;i++)
    {
        var li=document.createElement('li');
        li.className="work-item"
        //li.style.position='absolute';
        link = document.createElement('a');
        link.setAttribute('href', 'single_image.html?imageId='+array.files[i]);
       /* link.onclick = function (this) { 
            console.log(this)
            return false;

        };*/
        
        var workImageDiv=document.createElement('div');
        workImageDiv.className='work-image';
        var workImageImg=document.createElement('img');
        workImageImg.src=url+array.files[i]+extension;
        //workImageDiv.appendChild(workImageImg);
        
        
       /* workCaption=document.createElement('div');
        workCaption.className="work-caption font-alt"

        workTitle=document.createElement('h3');
        workTitle.className="work-title";

        workDescr=document.createElement("div");
        workDescr.className="work-descr";

        workCaption.appendChild(workTitle);
        workCaption.appendChild(workDescr);
        */
        workImageDiv.appendChild(workImageImg)
        link.appendChild(workImageDiv);
        //link.appendChild(workCaption);
        li.appendChild(link);
        ul.appendChild(li);




    }
   
}

function onloadContent()
{
  fileUpload1()
  picturesGet();
}

function fileUpload1()
{
  var url = "http://localhost:5000/upload"
  const input = document.querySelector('#avatars');

// Listen for file selection event
input.addEventListener('change', (e) => {
    fileUpload(input.files[0]);
});

// Function that handles file upload using XHR
const fileUpload = (file) => {
    // Create FormData instance
    const fd = new FormData();
    fd.append('file', file);

    // Create XHR rquest
    const xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    var token=sessionStorage.getItem('token')
    
    xhr.setRequestHeader("Authorization", "Bearer "+token );
    
    // Log HTTP response
    xhr.onload = () => {
        console.log(xhr.response);
    };

    // Send XHR reqeust
    

    xhr.send(fd);
};
}
function picturesGet()
{










    var url = "http://localhost:5000/search";

    var xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    var token=sessionStorage.getItem('token')
    
    xhr.setRequestHeader("Authorization", "Bearer "+token );
    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        const responseObj = JSON.parse(xhr.responseText);
      if(xhr.status==200)
      {
        picturesShow(responseObj);
      }
     

    }};

    xhr.send(null);
}
function removeAllChildNodes(parent){
  while(parent.firstChild)
  {
    parent.removeChild(parent.firstChild)
  }
}