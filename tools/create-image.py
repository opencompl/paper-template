#!/usr/bin/env python3

from subprocess import run
import os
import math
import sys
import shutil

def getPageNumber(name):
    files = os.listdir(os.path.dirname(name))
    files = filter(lambda f: f.startswith(os.path.basename(name)), files)
    files = filter(lambda f: f.endswith('.png'), files)
    files = list(files)
    return len(files)

def removePNGFiles(directory, tmpOnly = False):
    files = os.listdir(directory)
    files = filter(lambda x: x.find(".png") != -1, files)
    if tmpOnly:
        files = filter(lambda x: x.find("-tmp") != -1, files)

    for f in files:
      os.remove(directory + '/' + f)

def createImageOfPaper(path, width = 7, pages = 21):
    removePNGFiles(os.path.dirname(path), tmpOnly=True)

    name = path

    cmd = ['convert', '-density', '150', path, '-resize', '40%', '-background', 'white', '-alpha', 'remove', '-alpha', 'off', name + "-tmp.png"]
    run(cmd)

    pageNumber = getPageNumber(path);
    if pageNumber == 1:
        shutil.copyfile(name + "-tmp.png", name + "-tmp-0.png")

    for i in range(pageNumber, pages):
        cmd = ['convert', '-size', '1020x1320', 'xc:white', name + '-tmp-' + str(i) + '.png']
        run(cmd)

    for row in range(0, math.ceil(pages / width)):
        cmd = ['convert']
        for imageId in range(row * width, min((row + 1) * width, pages)):
            cmd.append(name + "-tmp-" + str(imageId) + ".png")
        cmd.append("+append")
        cmd.append(name + "-tmp-row-" + str(row) + ".png")
        run(cmd)

    cmd = ['convert']
    for row in range(0, math.ceil(pages / width)):
      cmd.append(name + "-tmp-row-" + str(row) + ".png")
    cmd.append("-append")
    cmd.append(name + "-full.png")
    run(cmd)
    removePNGFiles(os.path.dirname(path), tmpOnly=True)

import argparse

parser = argparse.ArgumentParser(description='Create an Image of the paper')
parser.add_argument('filename')
args = parser.parse_args()

createImageOfPaper("./" + args.filename)
