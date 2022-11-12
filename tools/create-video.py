#!/usr/bin/env python3

from subprocess import run
import os
import math
import sys
import shutil
from git import Repo
import zipfile
from subprocess import DEVNULL, STDOUT, run
import concurrent.futures
import argparse
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import date, timedelta
from matplotlib.ticker import ScalarFormatter
import matplotlib.dates as mdates


def getPageNumber(name):
    cmd = "pdfinfo " + name + " | grep 'Pages' | awk '{print $2}'"
    res = os.popen(cmd).read().strip()
    if res == "":
        return 0
    return int(res)

def getPDFSize(name):
    cmd = "pdfinfo " + name + " | grep 'Page size'"
    res = os.popen(cmd).read().strip().split(" ")
    return (int(round(float(res[8]),0)), int(round(float(res[10]),0)))

def removePNGFiles(directory, tmpOnly = False):
    files = os.listdir(directory)
    files = filter(lambda x: x.find(".png") != -1, files)
    if tmpOnly:
        files = filter(lambda x: x.find("-tmp") != -1, files)

    for f in files:
      os.remove(directory + '/' + f)

def createImageOfPaper(path, width = 7, pages = 21):
    removePNGFiles(os.path.dirname(path))

    name = path

    pageNumber = getPageNumber(path);

    if pageNumber == 0:
        return

    grid = getGrid(pageNumber)

    width = grid[0]
    pages = grid[0] * grid[1]

    pdfSize = getPDFSize(path)

    targetPage = (3840, 2160)

    targetPdf = (targetPage[0] / grid[0], targetPage[1] / grid[1])
    densityWidth = 100 / pdfSize[0] * (targetPage[0] / grid[0]) / 100 * 72
    densityHeight = 100 / pdfSize[1] * (targetPage[1] / grid[1]) / 100 * 72

    density = min(densityWidth, densityHeight)
    rows = grid[1]

    cmd = ['convert', '-quality', '100', '-density', str(density), path, '-background', 'white', '-alpha', 'remove', '-alpha', 'off', name + "-tmp.png"]
    run(cmd)

    if pageNumber == 1:
        shutil.copyfile(name + "-tmp.png", name + "-tmp-0.png")

    for i in range(pageNumber, pages):
        cmd = ['convert', '-size', str(1458 / rows) + "x" + str(density * 10), 'xc:white', name + '-tmp-' + str(i) + '.png']
        run(cmd)

    for row in range(0, rows):
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

    for release in releases:
        shutil.copyfile(release, path + ("still-%05d.png" % idx))
        idx = idx + 1

def createVideo(path = ""):
    run(['rm', path + 'video.mp4'])
    cmd = ['ffmpeg', '-r', '2', '-pattern_type', 'glob', '-i', path + '*-files/paper.pdf-full.png', '-vcodec', 'libx264', '-crf', '25', '-pix_fmt', 'yuv420p', '-vf', 'scale=3840:2160:force_original_aspect_ratio=1,pad=3840:2160:(ow-iw)/2:(oh-ih)/2:white,format=rgb24', path + 'video.mp4']
    run(cmd)
    print(path + 'video.mp4')

def plotStatistics(commit, filename, branch, count):
    repo = Repo(".")
    commit_number = 0
    commits = list(repo.iter_commits(branch))
    end = date.fromtimestamp(commits[0].committed_date)
    start = date.fromtimestamp(commits[-1].committed_date)
    delta = end - start

    date_ticks = []
    for offset in range(delta.days+1):
        current = start + timedelta(days=offset)
        date_ticks.append(current)

    histogram = [0] * (delta.days+1)

    for commit in commits:
      commit_date = date.fromtimestamp(commit.committed_date)
      histogram[(commit_date - start).days] += 1

    fig, ax = plt.subplots(figsize=(5, 3))

    ax.bar(date_ticks, histogram, align='center', alpha=0.5)

    commit_date = date.fromtimestamp(commit.committed_date)
    delta = end - commit_date
    histogram_highlight = [0] * (delta.days+1)
    histogram_highlight[delta.days] = histogram[delta.days]

    ax.bar(date_ticks, histogram_highlight, align='center', alpha=0.5, color='red')
    ax = plt.gca()

    ax.set_yscale('log')
    sf = ScalarFormatter()
    sf.set_scientific(False)
    ax.yaxis.set_major_formatter(sf)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    plt.savefig(filename, dpi=300, transparent=True)

def createImage(data, branch, count):
    print(data)
    repo = Repo(".")
    commit_number = data[0]
    commit = data[1]
    filename = str(commit_number) + ".zip"
    dirname =  str(commit_number).zfill(5) + "-files"

    repo.git.archive(commit, '-o', filename)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(dirname)

    shutil.copyfile("Makefile", dirname + "/Makefile")
    shutil.copyfile(".latexmkrc", dirname + "/.latexmkrc")
    run(['make', '-C', dirname, "paper.pdf"], stdout=DEVNULL, stderr=STDOUT)
    createImageOfPaper(dirname + "/paper.pdf")
    plotStatistics(commit,  dirname + "/statistics.png", branch, count)
    run(['convert', '-gravity', 'SouthEast', dirname + '/paper.pdf-full.png',
        dirname + '/statistics.png', '-composite', dirname +
        '/paper.pdf-full.png'])

def createImages(branch, count):
    repo = Repo(".")
    commits = list(reversed(list(repo.iter_commits(branch, max_count=count))))
    items = zip(range(len(commits)), commits)

    def f(data):
        createImage(data, branch, count)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(f, items)

def getGrid(pages):
    import itertools
    import math
    potentialGrids = []
    ratioPaper = 1.4142
    ratioScreen = 3840 / 2160

    for y in range(1, math.ceil(math.sqrt(pages)) + 1):
        for x in itertools.count():
            if x * y >= pages:
                potentialGrids.append((x,y))
                break

    for (x, y) in potentialGrids.copy():
        potentialGrids.append((y, x))

    potentialGrids = set(potentialGrids)

    def getRatio(xy):
        width = xy[0]
        height = ratioPaper * xy[1]
        return abs(ratioScreen- (width/height))

    return min(potentialGrids, key=getRatio)

def testImages():
    for i in range(1, 27):
        testImageSize(i)

parser = argparse.ArgumentParser(
    prog = 'ltxrepo2mpg',
    description = 'Translate a git paper repository into a video')
parser.add_argument('-c', '--count', default=10000)
parser.add_argument('-b', '--branch', default='main')

args = parser.parse_args()


createImages(args.branch, args.count)
createVideo()
