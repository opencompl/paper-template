![Compile paper](../../workflows/Compile%20paper/badge.svg)

Download:
[Draft (with comments)](../../releases/latest/download/draft.pdf) |
[Paper](../../releases/latest/download/paper.pdf)

This repository serves as a template for writing computer science papers in LaTeX. It supports
the following features:

  - Automatic paper builds using GitHub Actions
  - Normal and Draft variants of the same paper
  - Automatically generate a source archive of the paper
    By running `create-source-archive.sh` a file `paper-source.zip` is
    generated that contains the paper latex sources.
  - Comments
    - Notes are in the margin to not change the length of the paper
    - Wide margins (that do not change the paper layout) to have plenty
      of room for comments
    - Pieces of text can be addressed specifically by underlining this text
    - Comments in float enviroments (e.g., figure)

