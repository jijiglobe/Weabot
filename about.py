#!/usr/bin/python
print 'Content-type: text/html\n\n'

import mod,cgi,cgitb

cgitb.enable()

print '''
<html>
<head>
<title>About</title>
<link rel="stylesheet" type="text/css" href="login.css">
<LINK REL="SHORTCUT ICON" HREF="favicon.png">
</head>
<body>
<center>
<br><br><br><br>
<h1>About</h1>
<br>
<p>
Welcome. Weeabot is a website created by Jion Fairchild and Wendy Zhang that funcitons as a blog and anime sharing site combined.
It features a personal homepage, six profile pictures to choose from, ability to view other users' posts, friend list, an anime database,
a rating system, your very own anime list, and many more things.
<br><br>
This website is powered by the server of Stuyvesant High School's CS Department.
</p>
</center>
</body>
</html>
    '''
