# Source Latex files
TEX_MAIN = paper.tex

TEX_MAIN_DRAFT = draft.tex
TEX_MAIN_PAPER = paper.tex
TEX_MAIN_BLIND = blind.tex
TEX_MAIN_CAMERA_ACM = cameraACM.tex

# Generate PDF files
PDF_DRAFT = draft.pdf
PDF_PAPER = paper.pdf
PDF_BLIND = blind.pdf
PDF_CAMERA_ACM = cameraACM.pdf

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

# grammar is a phony rule, it generates index.html
# from textidote
.PHONY: grammar

all: ${PDF_DRAFT} ${PDF_PAPER}

# spelling and grammar
grammar: paper.tex
	# check that textidote exists.
	@textidote --version
	# allowed to fail since it throws error if we have grammar mistakes
	-textidote --check en --output html paper.tex > index.html
	python3 -m http.server


${PDF_DRAFT}: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_DRAFT}

${PDF_PAPER}: ${TEX_MAIN_PAPER} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_PAPER}

${PDF_CAMERA_ACM}: ${TEX_MAIN_CAMERA_ACM} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_CAMERA_ACM}

draft: ${PDF_DRAFT}

blind: ${PDF_BLIND}

paper: ${PDF_PAPER}

cameraACM: ${PDF_CAMERA_ACM}

view-draft: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_DRAFT}

view-paper: ${TEX_MAIN_PAPER} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_PAPER}

view-camera-acm: ${TEX_MAIN_CAMERA_ACM} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_CAMERA_ACM}

clean:
	latexmk -C
