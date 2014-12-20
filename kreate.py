#!/usr/bin/python
print 'Content-type: text/html\n\n'

# Wendy Zhang, pd 2

import cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()

import md5
m=md5.new()

f=open("users.txt","r")
s=f.readlines()
f.close()
data=[]
for i in s:
    data.append(i.strip("\n").strip().split(":"))
if len(form)==0:
    print '''
<html>
<head>
<title>Create Account</title>
</head>
<body>
<center>
<br><br><br><br>
<h1>Create Account</h1>
<form action="create.py" method="post">
Username: <input type="text" name="username"><br>
Password: <input type="password" name="passwd"><br>
<input type="submit" value="Create Account">
</form>
<br><a href="login.py">Login</a>
</center>
</body>
'''
elif len(form)==1:
    print '''
<html>
<head>
<title>Create Account</title>
</head>
<body>
<center>
<br><br><br><br>
Please complete all fields.
</center>
</body>
'''
else:
    done='f'
    username=form['username'].value
    for i in username:
        if (ord(i)<ord('A') or (ord(i)>ord('Z') and ord(i)<ord('a')) or ord(i)>ord('z')) and done=='f':
            done='t'
            print "<html>\n<head>\n<title>Create Account</title>\n</head>\n<body>\n<center>\n<br><br><br><br>\nSpecial characters cannot be in username.\n</center>\n</body>"
    if done=='f':
        for i in data:
            if username==i[0]:
                done='t'
                print '''
<html>
<head>
<title>Create Account</title>
</head>
<body>
<center>
<br><br><br><br>
Username taken.
</center>
</body>
'''
        if done=='f':
            passwd=form['passwd'].value
            if len(passwd)<10:
                print "<center>\n<br><br><br><br>\nPassword must be longer than 9 characters.\n</center>"
            else:
                sp='f'
                up='f'
                lo='f'
                nu='f'
                for i in passwd:
                    if (ord(i)<ord('A') or (ord(i)>ord('Z') and ord(i)<ord('a')) or ord(i)>ord('z')) and i not in '1234567890':
                        sp='t'
                    elif i in '1234567890':
                        nu='t'
                    elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
                        up='t'
                    elif ord(i)>=ord('a') and ord(i)<=ord('z'):
                        lo='t'
                if sp=='f' or up=='f' or lo=='f' or nu=='f':
                    print "<center>\n<br><br><br><br>\nPassword must contain uppercase and lower case letters, a number, and a special character.\n</center>"
                else:
                    import md5
                    m= md5.new()
                    s=passwd
                    m.update(s)
                    hashed = m.hexdigest()
                    f=open("users.txt",'a')
                    f.write(username+':'+hashed+'\n')
                    f.close()
		    filenameplaceholder = open('users/'+username+'.txt','w')
		    filenameplaceholder = close()
                    print "<center>\n<br><br><br><br>\nSuccess.\n</center>"
