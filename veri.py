#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

a = ["parth"]
b = ["Parth@246810"]

form = cgi.FieldStorage()
user = form.getvalue('user')
passwd = form.getvalue('passwd')
if(user in a):
	if(passwd in b):
		final = sp.getoutput("cat /var/www/html/command.html")
	else:
		print("invalid password")
else:
	print("invalid username")

print(final)
