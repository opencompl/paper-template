# Source LaTeX files
TEX_MAIN_PAPER = paper.tex
TEX_MAIN_SUBMISSION = submission.tex

# Generated PDF files
PDF_PAPER := $(TEX_MAIN_PAPER:.tex=.pdf)
PDF_SUBMISSION := $(TEX_MAIN_SUBMISSION:.tex=.pdf)

# Resources
IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

.PHONY: all grammar paper submission view-paper view-submission clean

all: ${PDF_SUBMISSION} ${PDF_PAPER}

# spelling and grammar
grammar: $(TEX_MAIN_PAPER)
	# check that textidote exists.
  @textidote --version
	# allowed to fail since it throws error if we have grammar mistakes
  -textidote --check en --output html $< > index.html
	python3 -m http.server

refcheck: paper
	@grep -e 'refcheck.*Unused' paper.log

${PDF_PAPER}: ${TEX_MAIN_PAPER} ${IMAGES}
	latexmk ${TEX_MAIN_PAPER}

${PDF_SUBMISSION}: ${TEX_MAIN_SUBMISSION} ${IMAGES}
	latexmk ${TEX_MAIN_SUBMISSION}

paper: ${PDF_PAPER}

submission: ${PDF_SUBMISSION}

view-paper: ${TEX_MAIN_PAPER} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_PAPER}

view-submission: ${TEX_MAIN_SUBMISSION} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_SUBMISSION}

clean:
	latexmk -C
