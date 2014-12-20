#!/usr/bin/python
print 'Content-type: text/html\n\n'


import cgi,cgitb
cgitb.enable()

form = cgi.FieldStorage()

if len(form)==3:
	username=form['username'].value
	id=form['id'].value
	text=form['textBox'].value
	text=text.replace('\n','!n').replace('=','!eq')

	f=open("posts.txt",'r')
	s=f.readlines()
	f.close()
	posts=[]
	for i in s:
	    posts.append(i.strip('\n').strip().split('='))

	if len(posts)<=0:
	    postnum='1'
	else:
	    postnum=str(int(posts[len(posts)-1][0])+1)
	posts.append([postnum,username,text])

	fposts=''
	for i in posts:
	    fposts+='='.join(i)+'\n'

	f=open("posts.txt",'w')
	f.write(fposts)
	f.close()

	print '''
	<meta http-equiv="refresh" content="0; url=homepage.py?username='''+username+'&id='+str(id)+'''"/>'''
elif len(form)==2:
	username=form['username'].value
	id=form['id'].value
	print '''<meta http-equiv="refresh" content="0; url=homepage.py?username='''+username+'&id='+str(id)+'''"/>'''


