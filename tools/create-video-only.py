#!/usr/bin/env python3

from subprocess import run
import os
import math
import sys
import shutil

def getReleases(path):
    releases = os.listdir(path)
    releases = filter(lambda x: x.find('master-release') != -1, releases)
    releases = map(lambda x: x.replace('master-release-', ''), releases)
    releases = map(lambda x: int(x), releases)
    releases = list(releases)
    releases.sort()
    releases = map(lambda x: path + 'master-release-' + str(x) + "/blind.png", releases)
    releases = list(releases)
    releases = filter(os.path.exists, releases)
    releases = list(releases)
    return list(releases)

def moveImages(path):
    releases = getReleases(path)
    releases.append("./blind.pdf-full.png")
    print(releases)

    idx = 0
    for release in releases:
        shutil.copyfile(release, path + ("still-%05d.png" % idx))
        idx = idx + 1

def createVideo(path):
    run(['rm', path + 'video.mp4'])
    cmd = ['ffmpeg', '-r', '1', '-i', path + 'still-%05d.png', '-vcodec', 'libx264', '-crf', '25', '-pix_fmt', 'yuv420p', '-vf', 'scale=3840:2160', path + 'video.mp4']
    run(cmd)
    shutil.copyfile(path + "video.mp4", "blind.mp4")
    print(path + 'video.mp4')

import argparse

parser = argparse.ArgumentParser(description='Create a Video from a GitHub Release Download of tobiasgrosser/paper-template.')
parser.add_argument('repo', help='owner/repo, e.g., tobias-grosser/paper-template')

args = parser.parse_args()
imagePath = args.repo + "/refs/heads/"
moveImages(imagePath)
createVideo(imagePath)
