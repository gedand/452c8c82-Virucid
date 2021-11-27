function registrationPost(username, password){
    var formData = new FormData();

    formData.append("username", "sanyi");
    formData.append("password", "baa");

    var url = "http://localhost:5000/registration";

    var xhr = new XMLHttpRequest();
    xhr.open("POST",url);

    xhr.setRequestHeader("Content-Type", "multipart/form-data");

    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4){
            console.log(xhr.status);
            console.log(xhr.responseText);
        }
    }

    xhr.send(formData);

}