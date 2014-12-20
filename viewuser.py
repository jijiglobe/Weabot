#!/usr/bin/python
print 'Content-type: text/html\n\n'

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

import cgi,cgitb,mod
cgitb.enable()

form= cgi.FieldStorage()

if len(form)==1:
    user=form['user'].value
    f=open("posts.txt",'r')
    s=f.readlines()
    f.close()
    posts=[]
    for i in s:
        posts.append(i.strip('\n').strip().split('='))
    myp=[]
    for i in posts:
        if i[1]==user:
            myp.append(i[2].replace('!n','<br>').replace('!eq','='))
    print'''
<html>
<head>
<title>'''+user+'''</title>
<link rel="stylesheet" type="text/css" href="profile.css">
</head>
<body>
<center>
Welcome to '''+user+''''s homepage.
<br><br>'''+maketb(myp)+'''
<center>
</body>
</html>
'''
elif len(form)==3:
    username=form['username'].value
    user=form['user'].value
    id=form['id'].value
    magic = id
    f=open("posts.txt",'r')
    s=f.readlines()
    f.close()
    posts=[]
    for i in s:
        posts.append(i.strip('\n').strip().split('='))
    myp=[]
    for i in posts:
        if i[1]==user:
            myp.append(i[2].replace('!n','<br>').replace('!eq','='))
    f=open('users/'+username+'.txt','r')
    friends=f.readlines()
    f.close()
    found=False
    for i in friends:
        if i.strip('\n')==user:
            found=True
    if found==True:
        add=''
    elif found==False:
        add='''<a href="addfriend.py?username='''+username+'&friend='+user+'&id='+id+'''">Add friend</a>'''
    f=open("users.txt",'r')
    s=f.readlines()
    f.close()
    users=[]
    for i in s:
        users.append(i.strip('\n').strip().split(':'))
    i=0
    while i<len(users):
        if users[i][0]==user:
            num=i
        i=i+1
        
    propic=users[num][3]
    desc=users[num][4].replace('!n','<br>').replace('!col',':')
    print '''
<html>
<head>
<title>'''+user+'''</title>
<link rel="stylesheet" type="text/css" href="profile.css">
<LINK REL="SHORTCUT ICON" HREF="favicon.png">
</head>
<body>
'''+mod.nav()+'''
<table class="hometable" width="100%">
<tr>
<td valign="top" align="left" width="40%">
<img src="../pics/propics/'''+propic+'''.jpg" width="230px">
<br><b>'''+user+'''</b><br>
<br><br><a href="viewlist.py?username='''+username+'&id='+magic+'&user='+user+'"> Click here to see '+user+''''s anime list</a><br><br>
'''+add+'''
<br><br>
'''+desc+'''
</td>
<td width="60%" valign="top">
'''+maketb(myp)+'''
</td>
</tr>
</table>
</body>
</html>
'''
