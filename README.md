![Compile paper](../../workflows/Compile%20paper/badge.svg)

Download:
[Draft](../../releases/latest/download/paper.pdf) |
[Blind (for submission)](../../releases/latest/download/blind.pdf) |
[Camera-Ready](../../releases/latest/download/camera.pdf) |
[Paper Source Archive](../../releases/latest/download/paper-source.zip) |

![Blind Paper](../../releases/latest/download/blind.png)

This repository serves as a template for writing computer science papers in LaTeX. It supports
the following features:

  - Automatic paper builds using GitHub Actions
  - Different variants of the same paper
    - Draft: Comments, wider margins, ...
    - Grammarly: Draft without word-brakes and single-column to copy-paste into http://grammarly.com
    - Blind: No comments, anonymous for double-blind review
    - Camera: No comments, with author names for camery-ready publication
  - Automatically generate a source archive of the paper
    By running `create-source-archive.sh` a file `paper-source.zip` is
    generated that contains the paper latex sources.
  - Comments
    - Notes are in the margin to not change the length of the paper
    - Wide margins (that do not change the paper layout) to have plenty
      of room for comments
    - Pieces of text can be addressed specifically by underlining this text
    - Comments in float enviroments (e.g., figure)
