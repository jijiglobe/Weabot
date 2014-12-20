#!/usr/bin/python
print 'content-type: text/html'
print

import mod,cgitb
cgitb.enable()
if mod.checklog():
	mod.swagin()
	username = mod.par('username')
	magic = mod.par('id')
	print '''
<html>
<head>
<title>Home</title>
<link rel="stylesheet" type="text/css" href="profile.css">
<LINK REL="SHORTCUT ICON" HREF="favicon.png">
</head>
<body>
'''+mod.nav()+'''
<center>
<form action="addfunc.py" method="get">
Name of Show:<input type="text" name="showname"><br><br>
Synopsis (optional):<br>
<textarea name="synopsis" cols="50" rows="5"></textarea>
<input type="hidden" name="username" value="'''+username+'''">
<input type="hidden" name="id" value="'''+magic+'''"><br>
<table class="hometable"><col width="400"><tr><td><font size="1">
* Please be respectful and add shows that exist. Try to use the original Japanese name and capitalize the first letter of each word. Any griefers will be banished for eternity
</font></td></td></table>
<input type="submit" value="Make Post" class="post">
</form>
</center></body></html>'''
