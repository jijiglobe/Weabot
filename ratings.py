#!/usr/bin/python
# -*- coding: cp936 -*-
print 'content-type: text/html'
print

import cgi,mod,os,cgitb
cgitb.enable()

if mod.checklog():
        mod.swagin()
        anime = mod.par('anime')
        magic = mod.par('id')
	username = mod.par('username')
        mylistfile = open('lists/'+username,'r')
	mylist = mylistfile.read()
	mylist = mylist.split('\n<li>')
	for x in range(len(mylist)):
		mylist[x] = mylist[x].split('status:')[0]
	infofile = open('info/'+anime,'r')
        info = infofile.read()
#        print info
        info = info.split('\nINFOSPLIT\n')
#        print info
        name = info[0]
        synopsis = info[2]
	if synopsis == '':
		synopsis = '-'
	ratings = info[1]
        average = 0
	if ratings != '':
        	for x in ratings.split('\n')[1:]:
                	average+=int(x)
        	average = round(average/(len(ratings.split('\n'))-1))
        mod.style('profile.css',anime)
        print mod.nav()
        print '<center><h3>"'+anime+'"</h3><br>'
        print '<h4>Rating: '+str(average)+'/10</h4>'
        print '<h4>Synopsis</h4><br>'
        print synopsis
	if username not in info[3].split('\n'):	
        	print '<form action="makerating.py">\n<h4>Leave a Rating: </h4><select name="rate">'
        	for x in range(11):
        	        print '<option value="'+str(x)+'">'+str(x)+'/10</option>'
        	print '''</select><br>
<input type="hidden" name="username" value="'''+username+'''">
<input type="hidden" name="id" value="'''+magic+'''"><br>
<input type="hidden" name="anime" value="'''+anime+'''">
<input type="submit" class="confirm">
</form><br>'''
	if anime not in mylist:
		print '<br><a href="addlist.py?anime='+anime+'&username='+username+'&id='+magic+'" > Add This Show To Your List</a>'
        print '</center></body></html>'
