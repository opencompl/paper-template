#!/usr/bin/env python3

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def setGlobalDefaults():
    ## Use TrueType fonts instead of Type 3 fonts
    #
    # Type 3 fonts embed bitmaps and are not allowed in camera-ready submissions
    # for many conferences. TrueType fonts look better and are accepted.
    # This follows: https://www.conference-publishing.com/Help.php
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42


setGlobalDefaults()

matplotlib.rcParams['figure.figsize'] = 5, 2

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [1.5, 1.2, 1.3, 1.1, 1.0]
women_means = [1.8, 1.5, 1.1, 1.3, 0.9]

# Color palette
light_gray = "#cacaca"
dark_gray = "#827b7b"
light_blue = "#a6cee3"
dark_blue = "#1f78b4"
light_green = "#b2df8a"
dark_green = "#33a02c"
light_red = "#fb9a99"
dark_red = "#e31a1c"

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means, width, label='Men', color=light_blue)
rects2 = ax.bar(x + width / 2,
                women_means,
                width,
                label='Women',
                color=dark_blue)

# Y-Axis Label
#
# Use a horizontal label for improved readability.
ax.set_ylabel('Speedup',
              rotation='horizontal',
              position=(1, 1.05),
              horizontalalignment='left',
              verticalalignment='bottom')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend(ncol=100,
          frameon=False,
          loc='lower right',
          bbox_to_anchor=(0, 1, 1, 0))

# Hide the right and top spines
#
# This reduces the number of lines in the plot. Lines typically catch
# a readers attention and distract the reader from the actual content.
# By removing unnecessary spines, we help the reader to focus on
# the figures in the graph.
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            '{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 1),  # 1 points vertical offset
            textcoords="offset points",
            fontsize="smaller",
            ha='center',
            va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

filename = os.path.basename(__file__).replace(".py", ".pdf")

# Do not emit a creation date. This will make the content of
# the pdfs we generate more deterministic.
metadata = {'CreationDate': None}

fig.savefig(filename, metadata=metadata)
