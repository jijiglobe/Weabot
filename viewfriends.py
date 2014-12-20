#!/usr/bin/python
print 'Content-type: text/html\n\n'


import cgi,cgitb,mod
cgitb.enable()

form = cgi.FieldStorage()

username=form['username'].value
id=form['id'].value

f=open('users/'+username+'.txt','r')
friends=f.readlines()
f.close()

def mktbfriends(l):
    ans='<table border="25" width="100%" style="border:25 solid #D7621D">\n<col width="20%"><col width="20%"><col width="20%"><col width="20%"><col width="20%">'
    x=0
    while x<len(l):
        i=0
        ans+='<tr>\n'
        while i<5 and x<len(l):
            ans+='<td height="50"><a href="viewuser.py?username='+username+'&user='+l[x]+'&id='+id+'">'+l[x]+'</a></td>\n'
            i+=1
            x+=1
        ans+='</tr>'
    return ans

print '''
<html>
<head>
<title>My friends</title>
<link rel="stylesheet" type="text/css" href="profile.css">
<LINK REL="SHORTCUT ICON" HREF="favicon.png">
</head>
<body>
'''+mod.nav()+'''
<br>'''+mktbfriends(friends)+'''
</body>
</html>'''

