PROJECTNAME = skeleton

PDF = ${PROJECTNAME}.pdf
TEX_MAIN = ${PROJECTNAME}.tex

all: ${PDF}

${PDF}: ${TEX_MAIN}
	pdflatex ${TEX_MAIN}
