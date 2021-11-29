

function RegisterValidationForm() {


    let username = document.forms["RegisterForm"]["Username"];
    let email = document.forms["RegisterForm"]["Email"];
    let password = document.forms["RegisterForm"]["Password"];
    let rePassword = document.forms["RegisterForm"]["RePassword"];

    if(username.value == "") {
      alert("Please enter your name.");
      username.focus();
      return false;
    }
    if(email.value == "") {
      alert("Please enter a valid e-mail address.");
      email.focus();
      return false;
    }
    if(email.value.indexOf("@", 0) < 0) {
      alert("Please enter a valid e-mail address.");
      email.focus();
      return false;
    }
    if(email.value.indexOf(".", 0) < 0) {
      alert("Please enter a valid e-mail address.");
      email.focus();
      return false;
    }
    if(password.value == "") {
      alert("Please enter your password");
      password.focus();
      return false;
    }
    if(password.value != rePassword.value) {
      alert("Password and confirm password not the same");
      rePassword.focus();
        return false;
      }
   /*   if(CheckPasswordStrength(password.value)<2){
          alert("A jelszónak tartalmaznia kell legalább 1db kis-, 1db nagy betűt,és 1 számot")
          pass.focus();
          return false
      }*/
      
      
    registrationPost(username.value,password.value);
  }
  function LoginValidationForm()
  {
    let username = document.forms["LoginForm"]["Username"];
    let password = document.forms["LoginForm"]["Password"];

    if(password.value == "") {
        alert("Please enter your password");
        pass.focus();
        return false;
      }
      if(username.value == "") {
        alert("Please enter your username.");
        username.focus();
        return false;
      }

      loginPost(username.value,password.value);

  }
  function CheckPasswordStrength(password) {
    var password_strength = document.getElementById("password_strength");

    //TextBox left blank.
    if (password.length == 0) {
        password_strength.innerHTML = "";
        return;
    }

    //Regular Expressions.
    var regex = new Array();
    regex.push("[A-Z]"); //Uppercase Alphabet.
    regex.push("[a-z]"); //Lowercase Alphabet.
    regex.push("[0-9]"); //Digit.
    regex.push("[$@$!%*#?&]"); //Special Character.

    var passed = 0;

    //Validate for each Regular Expression.
    for (var i = 0; i < regex.length; i++) {
        if (new RegExp(regex[i]).test(password)) {
            passed++;
        }
    }

    //Validate for length of Password.
    if (passed > 2 && password.length > 8) {
        passed++;
    }

    //Display status.
    var color = "";
    var strength = "";
    switch (passed) {
        case 0:
        case 1:
            strength = "Weak";
            color = "red";
            break;
        case 2:
            strength = "Good";
            color = "darkorange";
            break;
        case 3:
        case 4:
            strength = "Strong";
            color = "green";
            break;
        case 5:
            strength = "Very Strong";
            color = "darkgreen";
            break;
    }
    password_strength.innerHTML = strength;
    password_strength.style.color = color;
    return passed
}

function uploadPost(imageName)
{
    var url = "http://localhost:5000/upload";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
    }};

    var data = `{
    "file":"sanyiq"
    }`;
    xhr.send(data);
}

function registrationPost(username,password)
{
    var formData = new FormData();

    formData.append("username", username);
    formData.append("password", password); 

    var url = "http://localhost:5000/registration";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    xhr.onreadystatechange = function () {
      const responseObj = JSON.parse(xhr.responseText);
    if (xhr.readyState === 4) {
      if(responseObj.status=="success")
      {
        alert(responseObj.message);
      }
      else
      {
        console.log(responseObj.status);
        console.log(responseObj.message);
        alert(responseObj.message);
      }

    }};


    xhr.send(formData);
}

function deleteImagePost(fileId)
{
    var url = "http://localhost:5000/delete";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
    }};

    var data = `{
        {'fileid': '1'}
    }`;
    xhr.send(data);
}
function loginPost(username,password)
{
  var formData = new FormData();

    var url = "http://localhost:5000/login";
    var data = {};
    data.username=username;
    data.password=password;
    //formData.append("username", username);
    //formData.append("password", password); 
    jsonData=JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);
    xhr.setRequestHeader("Content-Type", "application/json");


    xhr.onreadystatechange = function () {
      const responseObj = JSON.parse(xhr.responseText);
    if (xhr.readyState === 4) {
      if(xhr.status==200)
      {
        sessionStorage.setItem('token', responseObj.access_token);
        window.location.href = 'index.html';
      }
      else
      {
        //console.log(responseObj.status);
        //console.log(responseObj.message);
        alert("Username or Password is incorrect");
      }

    }};
    xhr.send(jsonData);
}

function commentPost(username,password)
{

    var url = "http://localhost:5000/comment";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
    }};

    var data = `{
        'fileid': '1', 'comment': 'de rusnya :*'
    }`;
    xhr.send(data);
}

