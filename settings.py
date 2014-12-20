#!/usr/bin/python
print 'content-type: text/html'
print

import mod,cgitb,cgi
cgitb.enable()

if mod.checklog():
        mod.swagin()
        magic = mod.par('id')
        username = mod.par('username')
        mod.style('profile.css','Settings')
        print mod.nav()
        print'''
<table class="hometable">
<tr>
<td>
<h2>Settings</h2>
Name: '''+username+'''<br>
<form action="changesettings.py">
Description:<br><textarea name="description" cols="50" rows="5"></textarea><br>
Profile picture:<br>
<input type="radio" name="propic" value="bear"><img src="../pics/propics/bear.jpg" width="200px"><br><br>
<input type="radio" name="propic" value="cat"><img src="../pics/propics/cat.jpg" width="200px"><br><br>
<input type="radio" name="propic" value="dog"><img src="../pics/propics/dog.jpg" width="200px"><br><br>
<input type="radio" name="propic" value="rabbit"><img src="../pics/propics/rabbit.jpg" width="200px"><br><br>
<input type="radio" name="propic" value="snake"><img src="../pics/propics/snake.jpg" width="200px"><br><br>
<input type="radio" name="propic" value="stag"><img src="../pics/propics/stag.jpg" width="200px"><br><br>
<input type="hidden" name="username" value="'''+username+'''">
<input type="hidden" name="id" value="'''+magic+'''">
<input type="submit" class="confirm">
</td>
</tr>
</table>
</body>
</html>
'''
