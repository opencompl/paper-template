![Compile paper](../../workflows/Compile%20paper/badge.svg)

Download:
[Paper (with comments)](../../releases/latest/download/paper.pdf)
[Submission (without comments)](../../releases/latest/download/submission.pdf) |

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
  - Fonts
    - The [ACMart fonts](https://github.com/opencompl/paper-template/blob/master/acmart.cls#L720-L728)
      use [Inconsolata](https://ctan.org/pkg/inconsolata?lang=en) for monospace, 
      [Libertine](https://ctan.org/pkg/libertine?lang=en) for serif, and [newtx](https://ctan.org/pkg/newtx?lang=en) for math.
    - The Libertine `ttf` can be obtained as "linux libertine" on distros, and Inconsolata `ttf` as "Inconsolata".
    - The default font size of the body is `11pt`.
  - Figures
    - The paper is of A4 size, which in *physical units* is `210 x 297 mm`.
    - Choose figure size in *physical units* (`mm`/`inch`) based on how much of A4 it occupies and export to PDF.
    - Import figure PDF into paper using `\includegraphics{path/to/figure}`. This occupies the desired space in the paper; there is need to use
      `\includegraphics[width=<insert-width-here>]{path/to/figure}`. 
