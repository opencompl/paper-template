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

# Notes

- For `minted` version 3, users are required to add the following to their `${HOME}` or `TEXMFHOME` directory in a file 
  named `.latexminted_config`:

  ```json
  {
    "security": {
      "enable_cwd_config": true
    }
  }
  ```

  This is due to the fact that `minted` restricts shell execution of custom lexers by default for security reasons
  (i.e., arbitrary code execution).

  Moreover, the `minted` package requires each custom lexer to be listed by name and associated with its SHA256 hash of
  its containing file in a `.latexminted_config` file at the top of the paper template directory. We provide this 
  configuration, and a way to update it upon updating/adding the lexers by running the following command:

  ```bash
  tools/generate_lexers_json.py
  ```
