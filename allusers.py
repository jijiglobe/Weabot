#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi,cgitb,mod
cgitb.enable()

form= cgi.FieldStorage()

if len(form)>0:
    username=form['username'].value
    id=form['id'].value

    f=open('users.txt','r')
    s=f.readlines()
    f.close()
    users=[]
    for i in s:
        users.append(i.strip('\n').strip().split(':')[0])
    users.sort()

    print '''
    <html>
    <head>
    <title>View Users</title>
    <link rel="stylesheet" type="text/css" href="profile.css">
    <LINK REL="SHORTCUT ICON" HREF="favicon.png">
    '''+mod.nav()+'''
    </head>
    <body>
    '''

    if len(form)>0:
        print '<table class="hometable"><tr><td>'
        for i in users:
            print '''<a href="viewuser.py?user='''+i+'&username='+username+'&id='+id+'''">'''+i+'''</a><br>\n'''
        print '</td></tr></table>'
    else:
        print '<table class="hometable"><tr><td>'
        for i in users:
            print '''<a href="viewuser.py?user='''+i+'''">'''+i+'''</a><br>\n'''
        print '</td></tr></table>'

    print '''
</body>
</html>
'''
