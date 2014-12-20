from random import randint
import cgi,os,time

#Retrieves and returns the value of the 'name' parameter fromt the url string
def par(name):
	return cgi.FieldStorage()[name].value
#logs in user, updates timestamp for login and returns users 'magic' id
def yologin(formdata):
        logs = open('loggedin.txt','r')
        logged = logs.read()
        loglist = logged.split(',')
        logs.close()
        logss = open('loggedin.txt','w')
        found = False
	params = formdata
	uid = str(randint(0,9999999999))
        for x in loglist:
                if x.split(':')[0] == params['username'].value:
                        loglist.remove(x)
        logss.write(params['username'].value+':'+os.environ["REMOTE_ADDR"]+':'+uid+':'+str(time.time())+'\n')

        for x in loglist:
                logss.write(x+'\n')
        logss.close()
	return uid

#swagin is similar to yologin but does not updat the users 'magic' id use yologin on the login screen and then run swagin at the beginning of every page file.
def swagin():
        logs = open('loggedin.txt','r')
        logged = logs.read()
        loglist = logged.split(',')
        logs.close()
        logss = open('loggedin.txt','w')
        found = False
	params = cgi.FieldStorage()
        for x in loglist:
                if x.split(':')[0] == par('username'):
                        loglist.remove(x)
        logss.write(params['username'].value+':'+os.environ["REMOTE_ADDR"]+':'+par('id')+':'+str(time.time())+'\n')

        for x in loglist:
                logss.write(x+'\n')
        logss.close()

#a helper function for checklog
def isloggedin():
	user = par('username')
	logid = par('id')
	ipadress = os.environ["REMOTE_ADDR"]
	timenow = time.time()
	listoflogins = open('loggedin.txt','r')
	lis = listoflogins.read()
	lis = lis.split('\n')
	for x in lis:
		if x=='':
			break
		data = x.split(':')
		fuser = data[0]
		fid = data[2]
		fip = data[1]
		ftime = data[3]
		if user == fuser and logid == fid and ipadress == fip:
			if float(timenow) - float(ftime) < 900:
				return 0
			else:
				return 1
	return 2

#checks if the user has done anything in the last 15 minutes and prints an error if not, it also returns False
def checklog():
	if isloggedin() == 0:
		return True
	elif isloggedin() == 1:
		print 'Your session has timed out due to inactivity: click <a href="login.py">here</a> to log in again</a>'
		return False
	else:
		print 'You are not yet logged in on this computer: click <a href="login.py">here</a> to log in</a>'
		return False

#creates the head section of a py file. linking it to a css sheet at thed 1st parameters location and setting the title to the second parameter. also opens the body tag
def style(filename,title):
	print '<html><head>'
	print '<link rel="stylesheet" type="text/css" href="'+filename+'">'
	print '<LINK REL="SHORTCUT ICON" HREF="favicon.png">'
	print '<title>'+title+'</title>'
	print '</head><body>'

#returns the parametern nested in td tags
def d(DATA):
	return '<td>'+DATA+'</td>'


def nav():
        username=par('username')
        userid=par('id')
        return '''<table class="hometable" width="100%"><col width="260"><tr><td valign="top">

<a href="homepage.py?username='''+username+'''&id='''+userid+'''" class="navhome" title="Home"></a>
<a href="allusers.py?username='''+username+'''&id='''+userid+'''" class="navallusers" title="All Users"></a>
<a href="viewfriends.py?username='''+username+'''&id='''+userid+'''" class="navfriends" title="Friends"></a>
<a href="animelist.py?username='''+username+'''&id='''+userid+'''" class="navanimelist" title="Anime Ranking"></a>
<a href="settings.py?username='''+username+'''&id='''+userid+'''" class="navsettings" title="Settings"></a>
<a href="login.py" class="navlogout" title="Logout"></a>
</td>
<td valign="top">
<div style="line-height:5px"><br></div>
<form action="animelist.py" method="get">
<input type="hidden" name="username" value="'''+username+'''">
<input type="hidden" name="id" value="'''+userid+'''">
<input type="text" name="query" placeholder="Search anime" valign="bottom">
<input type="submit" class="search" valign="bottom">
</form>
</td><td align="right"><h1><font size="40"
style="-webkit-touch-callout: none;
-webkit-user-select: none;
-khtml-user-select: none;
-moz-user-select: none;
-ms-user-select: none;
user-select: none;">Weeabot.</font></h1></td></tr></table>
'''
