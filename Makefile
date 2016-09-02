PROJECTNAME = paper-skeleton

PDF = ${PROJECTNAME}.pdf
TEX_MAIN = ${PROJECTNAME}.tex

all: ${PDF}

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

${PDF}: ${TEX_MAIN} ${IMAGES}
	pdflatex ${TEX_MAIN}
