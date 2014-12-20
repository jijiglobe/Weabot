#!/usr/bin/python
print 'content-type: text/html'
print

import mod,cgitb,cgi
cgitb.enable()

def l(DATA):
	return '<li>'+DATA+'</li>'
if mod.checklog():
	mod.swagin()
	user = mod.par('user')
	magic = mod.par('id')
	listfile = open('lists/'+user,'r')
	thelist = listfile.read()
	listfile.close()
	mod.style('profile.css',user+"'s List")
	print mod.nav()
	print '<h2>'+user+"'s anime list</h2>"
	if thelist != '':
		print '<ul>'
  	        thelist = thelist.split('\n<li>')
		for x in thelist:
			stuff = x.split('status:')
			listing = stuff[0]
			listing += '<br>Status: '+stuff[1]
			if stuff[1] == 'Watching':
				listing += '<br>Seen '+stuff[2]+' episodes'
			print l(listing)
	else:
		print '<h3>'+user+' has not added any shows to their watch list yet</h3>'	
	print '</body></html>'

