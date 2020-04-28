# Source Latex files
TEX_MAIN = ${PROJECTNAME}.tex

TEX_MAIN_DRAFT = paper.tex
TEX_MAIN_GRAMMARLY = grammarly.tex
TEX_MAIN_BLIND = blind.tex
TEX_MAIN_CAMERA = camera.tex

# Generate PDF files
PDF_DRAFT = paper.pdf
PDF_GRAMMARLY = grammarly.pdf
PDF_BLIND = blind.pdf
PDF_CAMERA = camera.pdf

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

all: ${PDF_DRAFT} ${PDF_GRAMMARLY} ${PDF_BLIND} ${PDF_CAMERA}

${PDF_DRAFT}: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_DRAFT}

${PDF_GRAMMARLY}: ${TEX_MAIN_GRAMMARLY} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_GRAMMARLY}

${PDF_BLIND}: ${TEX_MAIN_BLINE} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_BLIND}

${PDF_CAMERA}: ${TEX_MAIN_CAMERA} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_CAMERA}

draft: ${PDF_DRAFT}

draft: ${PDF_GRAMMARLY}

blind: ${PDF_BLIND}

camera: ${PDF_CAMERA}

view-draft: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_DRAFT}

view-grammarly: ${TEX_MAIN_BLIND} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_GRAMMARLY}

view-blind: ${TEX_MAIN_BLIND} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_BLIND}

view-camera: ${TEX_MAIN_CAMERA} ${TEX_MAIN} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_CAMERA}

clean:
	rm -rf ${DIFF_PREV_PDF} ; latexmk -C
