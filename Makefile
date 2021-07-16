# Source Latex files
TEX_MAIN = paper.tex

TEX_MAIN_DRAFT = draft.tex
TEX_MAIN_GRAMMARLY = grammarly.tex

# Generate PDF files
PDF_DRAFT = draft.pdf
PDF_PAPER = paper.pdf
PDF_GRAMMARLY = grammarly.pdf

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

# spag is a phony rule, it generates index.html
# from textidote
.PHONY: spag


all: ${PDF_PAPER}

# spelling and grammar
spag: paper.tex
	# check that textidote exists.
	@textidote --version
	# allowed to fail since it throws error if we have grammar mistakes
	-textidote --check en --output html paper.tex > index.html
	python3 -m http.server


${PDF_DRAFT}: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_DRAFT}

${PDF_GRAMMARLY}: ${TEX_MAIN_GRAMMARLY} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_GRAMMARLY}

${PDF_PAPER}: ${TEX_MAIN_PAPER} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_PAPER}

draft: ${PDF_DRAFT}

grammarly: ${PDF_GRAMMARLY}

paper: ${PDF_PAPER}

view-draft: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_DRAFT}

view-grammarly: ${TEX_MAIN_BLIND} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_GRAMMARLY}

view-paper: ${TEX_MAIN_PAPER} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_PAPER}

clean:
	latexmk -C
