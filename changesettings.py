#!/usr/bin/python
print 'content-type: text/html'
print

import mod,cgitb,cgi
cgitb.enable()

form = cgi.FieldStorage()
username=form['username'].value
userid=form['id'].value
if mod.checklog() and len(form)==4:
        mod.swagin()
        username=form['username'].value
        userid=form['id'].value
        propic=form['propic'].value
        desc=form['description'].value
        desc=desc.replace('\n','!n').replace(':','!col')
        
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
        
        users[num][3]=propic
        users[num][4]=desc
        final=[]
        for i in users:
            final.append(':'.join(i))
        final='\n'.join(final)
        f=open("users.txt",'w')
	f.write(final)
	f.close()
print '<meta http-equiv="refresh" content="0; url=settings.py?username='+ username + '&id='+ userid+'"/>'
