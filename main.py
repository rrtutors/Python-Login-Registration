import webbrowser
file = open("form.html", "w")

html_code = """<!DOCTYPE html>
<html>
<head>
<title>Log In & Registration form</title>
<link rel="stylesheet", href="style.css">
</head>
<body>

<form action="login_page.php" method="post">
  <h3> Login Form</h3> 
  <div class="container">
    <label for="uname"><b>Email:</b></label>
    <input type="email" placeholder="Enter Email" name="email" required>
    <br>
    <label for="pswdd"><b>Password:</b></label>
    <input type="password" placeholder="Enter password" name="passwd" required>
    <br>
    <label>
      <input type="checkbox" name="remember"> Keep me logged in
    </label>
    <br>
    <button type="submit">Login</button>
    <br>
    <span class="pswd">Forgot <a href="#">password?</a></span>
  </div>
</form>
<br>
<br>
<br>
<form action="register_page.php" method="post">

<h3> Registration Form</h3> 
  
  <div class="container">
    <label for="uname"><b>Email:</b></label>
    <input type="email" placeholder="Enter Email" name="email" required>
    <br>
    <label for="pswdd"><b>Password:</b></label>
     <input type="password" placeholder="Enter password" name="passwd" required>
    <br>
    <label for="pswdd"><b> Confirm Password:</b></label>
    <input type="password" placeholder="Confirm password" name="passwd" required>
  
    <br>
    <button type="submit">Register</button>
    <br>
    <span class="pswd">Already Registered <a href="#">Log in here?</a></span>
  </div>
</form>


</body>
</html>"""
file1 = open("style.css", "w")
css_code = """
form {
  border: 3px solid black;
}
input[type=email], input[type=password] {
  width: 40%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
h3{
text-align:center;
float:center;
font-weight:bold;
font-color: blue;
}
button {
  background-color: red;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 18%;
}
button:hover {
  opacity: 0.8;
}
.container {
  text-align: center;
  margin: 24px 0 12px 0;
}
img.logo {
  width: 22%;
  border-radius: 50%;
}
.container {
  padding: 16px;
}
}
"""

file.write(html_code)

file1.write(css_code)

file.close()
file1.close()
webbrowser.open_new_tab("form.html")