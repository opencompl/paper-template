# Source Latex files
TEX_MAIN_PAPER = paper.tex
TEX_MAIN_SUBMISSION = submission.tex

# Generate PDF files
PDF_PAPER = paper.pdf
PDF_SUBMISSION = submission.pdf

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

# grammar is a phony rule, it generates index.html
# from textidote
.PHONY: grammar

all: ${PDF_SUBMISSION} ${PDF_PAPER}

# spelling and grammar
grammar: paper.tex
	# check that textidote exists.
	@textidote --version
	# allowed to fail since it throws error if we have grammar mistakes
	-textidote --check en --output html paper.tex > index.html
	python3 -m http.server

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
