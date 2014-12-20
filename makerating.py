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
	rating = mod.par('rate')
	infofile = open('info/'+anime,'r')
	info = infofile.read()
	infofile.close()
	newfile = open('info/'+anime,'w')
	
	info = info.split('\nINFOSPLIT\n')
	ratings = info[1].split('\n')
	ratings.append(rating)
	ratings = '\n'.join(ratings)
	info[1] = ratings
	rated = info[2].split('\n')
	rated.append(username)
	rated = '\n'.join(rated)
	info[3] = rated
	info = '\nINFOSPLIT\n'.join(info)
	newfile.write(info)
	newfile.close()
	print '<head><title>Redirecting...</title></head><meta http-equiv="refresh" content="0; ratings.py?username='+form['username'].value+'&id='+magic+'&anime='+anime+'" />'
