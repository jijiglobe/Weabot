#!/usr/bin/python
print 'content-type: text/html'
print

import cgi,cgitb,md5,os
cgitb.enable()
m = md5.new()
params = cgi.FieldStorage()
usas = open("users.txt","r")
users = usas.read()
usas.close()
linkback = '\n<a href="create.py">go back</a>'
def val(key):
        return params[key].value
def isnum(s):
        if ord(s) >= 48 and ord(s) <= 57:
                return True
        return False
def islower(s):
        if ord(s) >= 97 and ord(s) <= 122:
                return True
        return False
def isupper(s):
        if ord(s) >= 65 and ord(s) <= 90:
                return True
        return False
def hasUpper(s):
        if s.lower() != s:
                return True
        else:
                return False
def hasLower(s):
        if s.upper() != s:
                return True
        else:
                return False
def hasnum(s):
        for x in s:
                if isnum(x):
                        return True
        return False

def isspec(s):
        if isupper(s):
                return False
        if islower(s):
                return False
        if isnum(s):
                return False
        return True
def hasspec(s):
        for x in s:
                if isspec(x):
                        return True
        return False
def goodpass(swag):
        return hasspec(swag) and hasLower(swag) and hasUpper(swag) and hasnum(swag)
def newuser(name):
        for x in users.split(','):
                if x.split(':')[0] == name:
                        return False
        return True
def checkblack():
        f=open('kuro.txt','r')
        black=f.read()
        f.close()
        black=black.split('\r\n')
        ip = os.environ["REMOTE_ADDR"]
        ip=str(ip)
#        print ip
#        print black
        return ip in black
def taken(u):
        f=open('users.txt','r')
        users=f.readlines()
        names=[]
        for i in users:
                names.append(i.split(':')[0])
        return u in names

print """<html><head><title>Make an account</title><link rel="stylesheet" type="text/css" href="login.css"><LINK REL="SHORTCUT ICON" HREF="favicon.png"><div align="right"><a href="about.py" target="_blank" class="link" align="right"></a></div></head><body>"""

if 'username' in params and 'password' in params and 'password2' in params:
        u = val('username')
        p = val('password')
        p2 = val('password2')
        if checkblack():
                print "You are banned from creating accounts."
        elif taken(u):
                print "Username taken."
        elif p2 != p:
                print "Passwords do no match"
        elif not newuser(u):
                print "The username "+u+" is already taken",linkback
        elif not hasspec(p):
            print "Your password must contain a special character",linkback
        elif not hasLower(p):
            print "Your password must contain a lower case letter",linkback
        elif not hasUpper(p):
            print "Your password must contain an upper case letter",linkback
        elif not hasnum(p):
            print "Your password must contain a number",linkback
        elif hasspec(u):
            print "Your username may not contain a special character",linkback
        elif len(p) < 10:
            print "Your password must be 10 or more characters",linkback
        else:
            print "Account created successfully"
            userfile = open("users.txt",'a')
            m = md5.new()
            m.update(p)
            digest = m.hexdigest()
            ip = os.environ["REMOTE_ADDR"]
            userfile.write(u+':'+digest+':'+ip+":bear:"+'\n')
            userfile.close()
            xylophone = open('users/'+u+'.txt','w')
            heiyo=open('lists/'+u,'w')
            print """\n<br><br><a href="login.py">Login</a>"""
else:
        print """
<center>
<br><br><br><br>
<h1>Create Account</h1>
<form action="create.py" method="post">
Username: <input type="text" name="username"><br>
Password: <input type="password" name="password"><br>
Confirm:&nbsp &nbsp&nbsp&nbsp<input type="password" name="password2"><br>
<input type="submit" value="Create Account!">
</form>
<a href="login.py">login</a>
</center>"""
print """</body></html>"""
