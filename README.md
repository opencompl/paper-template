![Compile paper](../../workflows/Compile%20paper/badge.svg)

Download:
[Paper (with comments)](../../releases/latest/download/paper.pdf)
[Submission (without comments)](../../releases/latest/download/submission.pdf) |


### Conference: ASPLOS

- Abstract: 2025-08-13T23:59:00-05:00
- Submission: 2025-08-20T23:59:00-05:00

### Paper Information

- Chat: 
- Lead:
- Senior Lead:

## Info about the Paper-Template repository

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

To periodically update your paper with the latest template changes after cloning this repository, you can run the 
following commands:

```bash
# add upstream (only required once)
git remote add upstream git@github.com:opencompl/paper-template.git

# periodically update
git fetch upstream
git merge upstream/main
```

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

## HotCRP CI/CD

This repository has support for opt-in automatic submission of `submission.pdf` to HotCRP on every push to main.
This requires setting up the submission in HotCRP first.

0. Assume the HotCRP site is hosted at https://asplos26.hotcrp.com
1. Create the paper submission on the HotCRP website. `HOTCRP_PID` is the paper's submission ID in the URL (eg. `https://asplos26.hotcrp.com/paper/HOTCRP_PID`)
2. Create an Authentication Token in HotCRP's **Account Settings**: (eg. `https://asplos26.hotcrp.com/profile/developer`)
3. Set up `.github/hotcrp.env` with the values from HotCRP, and set `HOTCRP_ACTION_UPLOAD_ENABLED=true` to enable uploading by GitHub Actions.

```sh
HOTCRP_SITE_URL=https://asplos26.hotcrp.com
HOTCRP_PID=TODO
HOTCRP_ACTION_UPLOAD_ENABLED=true # This toggle enables the GitHub workflow
```

4. Lastly, add the `HOTCRP_TOKEN` repository secret in GitHub under **Settings -> Secrets and variables -> Actions**.

The submission script can also be run locally instead of via GitHub actions.
Don't forget to provide the token in the environment.

```sh
HOTCRP_TOKEN=... bash tools/upload-to-hotcrp.sh .github/hotcrp.env
```
