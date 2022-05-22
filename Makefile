# Source Latex files
TEX_MAIN = paper.tex

TEX_MAIN_DRAFT = draft.tex
TEX_MAIN_GRAMMARLY = grammarly.tex
TEX_MAIN_BLIND = blind.tex
TEX_MAIN_CAMERA_IEEE = cameraIEEE.tex
TEX_MAIN_CAMERA_ACM = cameraACM.tex

# Generate PDF files
PDF_DRAFT = draft.pdf
PDF_PAPER = paper.pdf
PDF_GRAMMARLY = grammarly.pdf
PDF_BLIND = blind.pdf
PDF_CAMERA_IEEE = cameraIEEE.pdf
PDF_CAMERA_ACM = cameraACM.pdf

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

# grammar is a phony rule, it generates index.html
# from textidote
.PHONY: grammar

all: ${PDF_DRAFT} ${PDF_GRAMMARLY} ${PDF_PAPER} ${PDF_CAMERA_IEEE}

# spelling and grammar
grammar: paper.tex
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

${PDF_CAMERA_IEEE}: ${TEX_MAIN_CAMERA_IEEE} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_CAMERA_IEEE}

${PDF_CAMERA_ACM}: ${TEX_MAIN_CAMERA_ACM} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_CAMERA_ACM}

draft: ${PDF_DRAFT}

blind: ${PDF_BLIND}

grammarly: ${PDF_GRAMMARLY}

paper: ${PDF_PAPER}

cameraIEEE: ${PDF_CAMERA_IEEE}

cameraACM: ${PDF_CAMERA_ACM}

view-draft: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_DRAFT}

view-grammarly: ${TEX_MAIN_BLIND} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_GRAMMARLY}

view-paper: ${TEX_MAIN_PAPER} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_PAPER}

view-camera-ieee: ${TEX_MAIN_CAMERA_IEEE} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_CAMERA_IEEE}

view-camera-acm: ${TEX_MAIN_CAMERA_ACM} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_CAMERA_ACM}

clean:
	latexmk -C
