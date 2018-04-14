#!/usr/bin/env python

import os

directory = os.path.dirname(os.path.realpath(__file__))
directory = os.path.basename(directory)

projectname = directory

os.rename("paper-template.tex", projectname + ".tex")

f = open("Makefile",'r')
filedata = f.read()
f.close()

newdata = filedata.replace("paper-template", projectname)

f = open("Makefile.bak",'w')
f.write(newdata)
f.close()
os.rename("Makefile.bak", "Makefile")

f = open("README.md",'r')
filedata = f.read()
f.close()

newdata = filedata.replace("paper-template", projectname)

f = open("README.md.bak",'w')
f.write(newdata)
f.close()
os.rename("README.md.bak", "README.md")

f = open(".gitlab-ci.yml",'r')
filedata = f.read()
f.close()

newdata = filedata.replace("paper-template", projectname)

f = open(".gitlab-ci.yml.bak",'w')
f.write(newdata)
f.close()
os.rename(".gitlab-ci.yml.bak", ".gitlab-ci.yml")
