#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi,cgitb,mod
cgitb.enable()

form = cgi.FieldStorage()

def maketb(l):
    ans=''
    for i in l[::-1]:
        ans+='''
<table class="poststable" style="table-layout: fixed; width: 100%">\n<col width="100%">\n
<tr>
<td align="left" style="word-wrap: break-word">'''+i+'''</td>
</tr>
</table><br>
'''
    ans+='</table>'
    return ans

if len(form)<2:
    print '''
<html>
<head>
<title>Home</title>
</head>
<body>
Please log in.
</body>
</html>
'''

else:
    username=form['username'].value
    id=form['id'].value
    if mod.checklog():
        mod.swagin()
#    f=open(".logged.txt",'r')
#    s=f.readlines()
#    f.close()
#    loggedin=[]
#    for i in s:
#        loggedin.append(i.strip('\n').strip().split(':'))
#    match=False
#    for i in loggedin:
#        if username==i[0] and id==i[1] and ip==i[2]:
#            match=True
    f=open("posts.txt",'r')
    s=f.readlines()
    f.close()
    posts=[]
    for i in s:
        posts.append(i.strip('\n').strip().split('='))
    myp=[]
    for i in posts:
        if i[1]==username:
            myp.append(i[2].replace('!n','<br>').replace('!eq','='))
                
    f=open("users.txt",'r')
    s=f.readlines()
    f.close()
    users=[]
    for i in s:
        users.append(i.strip('\n').strip().split(':'))
    i=0
    while i<len(users):
        if users[i][0]==username:
            num=i
        i=i+1
        
    propic=users[num][3]
    desc=users[num][4].replace('!n','<br>').replace('!col',':')
    print '''
<html>
<head>
<title>Home</title>
<link rel="stylesheet" type="text/css" href="profile.css">
<LINK REL="SHORTCUT ICON" HREF="favicon.png">
</head>
<body>
'''+mod.nav()+'''
<table class="hometable" width="100%">
<tr>
<td valign="top" width="40%">
<img src="../pics/propics/'''+propic+'''.jpg" width="230px">
<br><b>'''+username+'''</b>
<br>
<a href="mylist.py?username='''+username+'&id='+id+'''">View my anime list</a>
<br><br>
'''+desc+'''
</td>
<td width="60%">
<center>
<form action=makepost.py method="post">
<textarea name="textBox" cols="50" rows="5"></textarea><br><br>
<input type="hidden" name="username" value="'''+username+'''">
<input type="hidden" name="id" value="'''+id+'''">
<input type="submit" value="Make Post" class="post">
</form>
</center>
'''+maketb(myp)+'''
</td>
</tr>
</table>
</body>
</html>
'''

