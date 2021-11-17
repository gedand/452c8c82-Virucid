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
      pass.focus();
      return false;
    }
    if(password.value != rePassword) {
        alert("Please enter your password");
        pass.focus();
        return false;
      }
      if(CheckPasswordStrength(password.value)<2){
          alert("A jelszónak tartalmaznia kell legalább 1db kis-, 1db nagy betűt,és 1 számot")
          pass.focus();
          return false
      }
    return true;
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