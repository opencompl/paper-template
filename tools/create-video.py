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
    print(path)
    removePNGFiles(os.path.dirname(path))

    name = path

    cmd = ['convert', '-density', '300', path, '-resize', '40%', '-background', 'white', '-alpha', 'remove', '-alpha', 'off', name + "-tmp.png"]
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

def getReleases(path):
    releases = os.listdir(path)
    releases = filter(lambda x: x.find('master-release') != -1, releases)
    releases = map(lambda x: x.replace('master-release-', ''), releases)
    releases = map(lambda x: int(x), releases)
    releases = list(releases)
    releases.sort()
    releases = map(lambda x: path + 'master-release-' + str(x) + "/blind.pdf", releases)
    releases = list(releases)
    releases = filter(os.path.exists, releases)
    releases = list(releases)
    return list(releases)

from multiprocessing import Pool

def createImages(path):
    releases = getReleases(path)

    with Pool(4) as p:
        p.map(createImageOfPaper, releases)

def moveImages(path):
    removePNGFiles(path)
    releases = getReleases(path)
    releases = map(lambda x: x + "-full.png", releases)
    releases = filter(os.path.exists, releases)

    idx = 0
    for release in releases:
        shutil.copyfile(release, path + ("still-%05d.png" % idx))
        idx = idx + 1

def createVideo(path):
    run(['rm', path + 'video.mp4'])
    cmd = ['ffmpeg', '-r', '1', '-i', path + 'still-%05d.png', '-vcodec', 'libx264', '-crf', '25', '-pix_fmt', 'yuv420p', '-vf', 'scale=3840:2160', path + 'video.mp4']
    run(cmd)
    print(path + 'video.mp4')

import argparse

parser = argparse.ArgumentParser(description='Create a Video from a GitHub Release Download of tobiasgrosser/paper-template.')
parser.add_argument('repo', help='owner/repo, e.g., tobias-grosser/paper-template')

args = parser.parse_args()
imagePath = args.repo + "/refs/heads/"
createImages(imagePath)
moveImages(imagePath)
createVideo(imagePath)
