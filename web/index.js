function picturesShow(array)
{
  var arr=["assets/images/work-2.jpg","assets/images/work-2.jpg","assets/images/work-2.jpg"];

    //var arr=['omae','mo','shindeiru'];
    var ul=document.getElementById('works-grid');
    removeAllChildNodes(ul);
    

    for(i=0; i<=arr.length-1;i++)
    {
        var li=document.createElement('li');
        li.className="work-item"
        //li.style.position='absolute';
        link = document.createElement('a');
        link.setAttribute('href', 'single_image.html?imageId='+arr[i]);
       /* link.onclick = function (this) { 
            console.log(this)
            return false;

        };*/
        
        var workImageDiv=document.createElement('div');
        workImageDiv.className='work-image';
        var workImageImg=document.createElement('img');
        workImageImg.src=arr[i];
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
function picturesGet(date1,date2)
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
        picturesShow(responseObj)
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