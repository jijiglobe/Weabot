#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi,cgitb,os,time,mod
cgitb.enable()

#returns wether or not a string is a subtring of an element in a list
def subinlist(string,l):
        for x in l:
                if string in x.lower():
                        return True
        return False

if mod.checklog():
	mod.swagin()
	malfile=open('mal','r')
	mal = malfile.read().split('\n')
	mal.sort()
	maldict = {}
	username = mod.par('username')
	form = cgi.FieldStorage()
	magic = mod.par('id')
#	mod.style('theprofile.css','List of Anime')


	print '''<html>
<head>
<title>Home</title>
<link rel="stylesheet" type="text/css" href="profile.css">
<LINK REL="SHORTCUT ICON" HREF="favicon.png">
</head>
<body>
'''+mod.nav()+'''
<center>
'''
	print '<br><br>'
	if 'query' in form:
		query = mod.par('query').lower()
		print 'you searched for:'+mod.par('query')+'<br><br>'
		print '<a href="animelist.py?username='+username+'&id='+magic+'''">See All Listings</a>
<br><br>
'''
		if subinlist(query,mal):
                        print '<table class="poststable" style="table-layout: fixed; width: 60%;">\n<col width="100%"><tr><td><center>'
			for x in mal:
				if query in x.lower():
					print '<a href="ratings.py?anime='+x+'&username='+mod.par('username')+'&id='+mod.par('id')+'"><font color="#D7621D">'+x+'</font></a></br>'
                        print '</center></td></tr></table>'
		else:
			print 'No titles containing your query were found'
	else:
                print '<table class="poststable" style="table-layout: fixed; width: 60%;">\n<col width="100%"><tr><td><center>'
		for x in mal:
			print '''<a href="ratings.py?anime='''+x+'&username='+mod.par('username')+'&id='+mod.par('id')+'"><font color="#D7621D">'+x+'''</font></a><br><br>'''
                print '</center></td></tr></table><br>'
	
	print '<br><br>'	
	print '<a href="addshow.py?username='+mod.par('username')+'&id='+mod.par('id')+'">Click Here To Add a New Show To The List</a>'	
	print '</body></html>'
