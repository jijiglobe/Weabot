#!/usr/bin/python
print 'content-type: text/html'
print

import mod,cgitb,cgi
cgitb.enable()

def l(DATA):
        return '<li>'+DATA+'</li>'
if mod.checklog():
        mod.swagin()
        username = mod.par('username')
        magic = mod.par('id')
        form = cgi.FieldStorage()
        if 'completed' in form:
                completed = mod.par('completed')
                listfile = open('lists/'+username,'r')
                thelist = listfile.read().split('\n<li>')
                listfile.close()
                for x in range(len(thelist)):
                        showdata = thelist[x].split('status:')
                        if showdata[0]==completed:
                                showdata[1] = 'Completed'
                                thelist[x] = 'status:'.join(showdata)
                                break
                editfile = open('lists/'+username,'w')
                editfile.write('\n<li>'.join(thelist))
                editfile.close()
        elif 'upto' in cgi.FieldStorage():
                completed = mod.par('show')
                listfile = open('lists/'+username,'r')
                thelist = listfile.read().split('\n<li>')
                listfile.close()
                upto = mod.par('upto')
                for x in range(len(thelist)):
                        showdata = thelist[x].split('status:')
                        if showdata[0]==completed:
                                showdata[2] = upto
                                thelist[x] = 'status:'.join(showdata)
                                break
                editfile = open('lists/'+username,'w')
                editfile.write('\n<li>'.join(thelist))
                editfile.close()
        listfile = open('lists/'+username,'r')
        thelist = listfile.read()
        listfile.close()
        mod.style('profile.css','My List')
        f=open("users.txt",'r')
        s=f.readlines()
        f.close()
        users=[]
        for i in s:
                users.append(i.strip('\n').strip().split(':'))
        i=0
        while i<len(users):
                if users[i][0]==username:
                    num=i
                i=i+1
        
        propic=users[num][3]
        desc=users[num][4].replace('!n','<br>').replace('!col',':')
        print mod.nav()
        print '''
<table class="hometable" width="100%">
<tr>
<td valign="top" width="40%">
<img src="../pics/propics/'''+propic+'''.jpg" width="230px">
<br><b>'''+username+'''</b>
<br><br>
'''+desc+'''
</td>
<td width="60%">
<center>
<h2> Your anime list</h2>'''
        if thelist != '':
#                print '<ol>'
                thelist = thelist.split('\n<li>')
                for x in thelist:
                        stuff = x.split('status:')
                        listing = '<table class="postable" border="25" class="postable" style="background-color:#D7621D;color:#FBF9F6;width:100%;border:25px solid #D7621D;"><tr><td>'+stuff[0]
                        listing += '<br>Status: '+stuff[1]
                        if stuff[1] == 'Watching':
                                listing += '<br>Seen '+stuff[2]+' episodes'
                                listing += '''<br><br>
<form action="mylist.py">
<input type="hidden" name="username" value="'''+username+'''">
<input type="hidden" name="id" value="'''+magic+'''">
<input type="hidden" name="completed" value="'''+stuff[0]+'''">
Completed? <input type="submit" value="Completed?" class="confirm">
</form>
'''
                                listing += '''
<form action="mylist.py">
<input type="hidden" name="username" value="'''+username+'''">
<input type="hidden" name="id" value="'''+magic+'''">
I've seen up to episode <input type="text" name="upto">
<input type="hidden" name="show" value="'''+stuff[0]+'''">
<input type="submit" value="Update" class="post">
</form>
'''
                        listing += '</td></tr></table>'
                        print l(listing)
        else:
                print '<h3> You have not added any shows to your watch list yet</h3>'   
        print '</center></td></tr></table></body></html>'
