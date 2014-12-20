#!/usr/bin/python
print 'content-type: text/html'
print

import mod,cgi,os,cgitb
cgitb.enable()
if mod.checklog():
	form = cgi.FieldStorage()
	mod.swagin()
	anime = mod.par('anime')
	magic = mod.par('id')
	username = mod.par('username')
	listfile = open('lists/'+username,'r')
	mylist = listfile.read()
	listfile.close()
	newfile = open('lists/'+username,'a')

	if mylist != '':
		newfile.write('\n<li>')
	newshow='status:'.join([anime,'Watching','1'])
	newfile.write(newshow)

	newfile.close()
	print '<head><title>Redirecting...</title></head><meta http-equiv="refresh" content="0; ratings.py?username='+form['username'].value+'&id='+magic+'&anime='+anime+'" />'


