#!/usr/bin/python
print 'content-type: text/html'
print

import mod,cgitb,cgi,os
cgitb.enable()

form = cgi.FieldStorage()
if mod.checklog():
        mod.swagin()
        mallist = open('mal','r')
        allanime=mallist.readlines()
        if not mod.par('showname') in allanime:
                ip = os.environ["REMOTE_ADDR"]
                log=open('addlog.txt','a')
                log.write(mod.par('username')+':'+str(ip)+':'+mod.par('showname')+'\n')
                log.close()
                
                mallist = open('mal','a')
                mallist.write('\n'+mod.par('showname'))
                mallist.close()
                info = open('info/'+mod.par('showname'),'w')
                data = []
                data.append(mod.par('showname'))
                data.append('')
                if len(form)==3:
                        data.append('-')
                else:
                        data.append(mod.par('synopsis'))
                data.append('')
                info.write('\nINFOSPLIT\n'.join(data))
                info.close()
                print '<meta http-equiv="refresh" content="0; url=animelist.py?username='+ mod.par('username') + '&id='+ mod.par('id')+'"/>'
