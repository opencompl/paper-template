PROJECTNAME = paper-template

PDF = ${PROJECTNAME}.pdf
DIFF_PREV_PDF = ${PROJECTNAME}-diff-prev-commit.pdf
TEX_MAIN = ${PROJECTNAME}.tex

all: ${PDF}

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

${PDF}: ${TEX_MAIN} ${IMAGES}
	latexmk -pdf

${DIFF_PREV_PDF}: ${TEX_MAIN} ${IMAGES}
	git latexdiff HEAD^ HEAD --main ${TEX_MAIN} --no-flatten -o ${DIFF_PREV_PDF}

clean:
	latexmk -C; rm ${PROJECTNAME}-prev-commit.pdf
