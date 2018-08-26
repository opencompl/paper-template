#!/usr/bin/env python

import os

directory = os.path.dirname(os.path.realpath(__file__))
directory = os.path.basename(directory)

projectname = directory

os.rename("paper-template.tex", projectname + ".tex")


def replaceFile(filename):
    f = open(filename,'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace("paper-template", projectname)

    f = open(filename + ".bak",'w')
    f.write(newdata)
    f.close()
    os.rename(filename + ".bak", filename)

replaceFile("Makefile")
replaceFile("README.md")
replaceFile(".gitlab-ci.yml")
replaceFile("paper-template-draft.tex")
replaceFile("paper-template-blind.tex")
replaceFile("paper-template-camera.tex")

os.rename("paper-template-draft.tex", projectname + "-draft.tex")
os.rename("paper-template-blind.tex", projectname + "-blind.tex")
os.rename("paper-template-camera.tex", projectname + "-camera.tex")

os.remove("initialize.py")
