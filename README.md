![Compile paper](../../workflows/Compile%20paper/badge.svg)

Download:
[Draft](../../releases/latest/download/paper.pdf) |
[Grammarly](../../releases/latest/download/grammarly.pdf) |
[Blind (for submission)](../../releases/latest/download/blind.pdf) |
[Camera-Ready](../../releases/latest/download/camera.pdf) |
[Paper Source Archive](../../releases/latest/download/paper-source.zip)

This repository serves as a template for writing computer science papers in LaTeX. It supports
the following useful features:

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
  - Paper Video
    Whenever a commit is tagged, the automatically built PDFs are combined into a release
    video that illustrates the writing process.
  - GitHub Pages Support
    - The rebuilt repository will be pushed to GitHub Pages to such that the PDFs are
      also available for users without a GitHub Account. The PDFs are availble as
      paper.pdf, grammarly.pdf, blind.pdf, and camera.pdf in the root folder of
      the GitHub page of this respository.

      WARNING: in case you use a private repository, you may need to push once manually
      to the gh-pages branch for the rebuilds to be triggered.
