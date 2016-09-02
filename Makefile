PROJECTNAME = paper-skeleton

PDF = ${PROJECTNAME}.pdf
TEX_MAIN = ${PROJECTNAME}.tex

all: ${PDF}

IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

${PDF}: ${TEX_MAIN} ${IMAGES}
	pdflatex ${TEX_MAIN} && bibtex ${PROJECTNAME} && \
        pdflatex ${TEX_MAIN} && pdflatex ${TEX_MAIN} 

clean:
	rm -rf *.pdf *.log *.aux *.bib
