#!/usr/bin/python
print 'Content-type: text/html\n\n'

#Wendy Zhang, pd 2

import md5
import mod
import cgitb
from random import randint
cgitb.enable()



import cgi,cgitb
cgitb.enable()

form = cgi.FieldStorage()



if len(form)==0:
    print '''
<html>
<head>
<title>Login</title>
<link rel="stylesheet" type="text/css" href="login.css">
<LINK REL="SHORTCUT ICON" HREF="favicon.png">
<div align="right"><a href="about.py" target="_blank" class="link" align="right"></a></div>
</head>
<body>
<center>
<br><br><br><br>
<h1>Login</h1><br>
<form action="login.py" method="post">
Username: <input type="text" name="username"><br>
Password: <input type="password" name="passwd"><br>
<input type="submit" value="Login">
</form>
<br><a href="create.py">Create Account</a>
</center>
</body>
</html>
    '''
  
def login(username,password):
    loginsfile=open("users.txt","r")
    logins = loginsfile.read().split('\n')
    logins=logins[0:len(logins)-1]
    m= md5.new()
    m.update(password)
    hashenter = m.hexdigest()
    for x in logins:
#	print x,'ABCD','<br>',
        user = x.split(':')[0]
#        print x.split(':')[1],'<br>'
#        hashed='123213'
        hashed = x.split(':')[1]
#	print password+'='+hashenter,'<br>',hashed,'<br>'
#	print user,'<br>',username,'<br>'
#	print 'AYEEE','<br><br>'
        if hashenter.strip() == hashed.strip() and user == username:
            return True

if 'username' in form and 'passwd' in form:
        w=form['passwd'].value
        m= md5.new()
        m.update(w)
        hashenter = m.hexdigest()
        if login(form['username'].value,form['passwd'].value):
                #print "<p>You have logged in successfully</p>"
                uid = mod.yologin(form)
                print '<head><title>Redirecting...</title></head><meta http-equiv="refresh" content="0; homepage.py?username='+form['username'].value+'&id='+uid+'" />'
        else:
                print "<p>Incorrect Username/Passowrd combination</p>"
                #print hashenter+'<br>'+form['user'].value
elif 'username' not in form and 'passwd' in form:
        print "<h1> ENTER A USERNAME!</h1>"
elif 'passwd' not in form and 'user' in form:
        print "<h1> ENTAR A PASSWORD!</h1>"


