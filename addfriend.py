#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi,cgitb
cgitb.enable()

form= cgi.FieldStorage()

username=form['username'].value
friend=form['friend'].value
id=form['id'].value

f=open('users/'+username+'.txt','a')
f.write(friend+'\n')
f.close

print '''
<html>
<head>
<title>Redirecting..</title>
<meta http-equiv="refresh" content="0; url=viewuser.py?username='''+username+'&user='+friend+'&id='+id+'''"/>
</head>
</html>
'''

