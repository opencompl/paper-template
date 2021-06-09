# Source Latex files
TEX_MAIN = paper.tex

TEX_MAIN_DRAFT = draft.tex
TEX_MAIN_GRAMMARLY = grammarly.tex
TEX_MAIN_BLIND = blind.tex
TEX_MAIN_CAMERA_IEEE = cameraIEEE.tex

# Generate PDF files
PDF_DRAFT = draft.pdf
PDF_PAPER = paper.pdf
PDF_GRAMMARLY = grammarly.pdf
PDF_BLIND = blind.pdf
PDF_CAMERA_IEEE = cameraIEEE.pdf

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

all: ${PDF_DRAFT} ${PDF_GRAMMARLY} ${PDF_PAPER} ${PDF_CAMERA_IEEE}

${PDF_DRAFT}: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_DRAFT}

${PDF_GRAMMARLY}: ${TEX_MAIN_GRAMMARLY} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_GRAMMARLY}

${PDF_PAPER}: ${TEX_MAIN_PAPER} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_PAPER}

${PDF_CAMERA_IEEE}: ${TEX_MAIN_CAMERA_IEEE} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_CAMERA_IEEE}

draft: ${PDF_DRAFT}

blind: ${PDF_BLIND}

grammarly: ${PDF_GRAMMARLY}

paper: ${PDF_PAPER}

cameraIEEE: ${PDF_CAMERA_IEEE}

view-draft: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_DRAFT}

view-grammarly: ${TEX_MAIN_BLIND} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_GRAMMARLY}

view-paper: ${TEX_MAIN_PAPER} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_PAPER}

view-camera-ieee: ${TEX_MAIN_CAMERA_IEEE} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_CAMERA_IEEE}

clean:
	latexmk -C
