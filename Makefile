PROJECTNAME = paper-template

# Source Latex files
TEX_MAIN = ${PROJECTNAME}.tex

TEX_MAIN_DRAFT = ${PROJECTNAME}-draft.tex
TEX_MAIN_BLIND = ${PROJECTNAME}-blind.tex
TEX_MAIN_CAMERA = ${PROJECTNAME}-camera.tex

# Generate PDF files
PDF_DRAFT = ${PROJECTNAME}-draft.pdf
PDF_BLIND = ${PROJECTNAME}-blind.pdf
PDF_CAMERA = ${PROJECTNAME}-camera.pdf

DIFF_PREV_PDF = ${PROJECTNAME}-diff-prev-commit.pdf

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

all: ${PDF_DRAFT} ${PDF_BLIND} ${PDF_CAMERA}

${PDF_DRAFT}: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_DRAFT}

${PDF_BLIND}: ${TEX_MAIN_BLINE} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_BLIND}

${PDF_CAMERA}: ${TEX_MAIN_CAMERA} ${TEX_MAIN} ${IMAGES}
	latexmk ${TEX_MAIN_CAMERA}

${DIFF_PREV_PDF}: ${TEX_MAIN_DRAFT} ${TEX_MAIN} ${IMAGES}
	git latexdiff HEAD^ HEAD --main ${TEX_MAIN_DRAFT} -o ${DIFF_PREV_PDF}

clean:
	rm -rf ${DIFF_PREV_PDF} ; latexmk -C
