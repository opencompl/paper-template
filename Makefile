# Source LaTeX files
TEX_MAIN_PAPER = paper.tex
TEX_MAIN_SUBMISSION = submission.tex

# Generated PDF files
PDF_PAPER := $(TEX_MAIN_PAPER:.tex=.pdf)
PDF_SUBMISSION := $(TEX_MAIN_SUBMISSION:.tex=.pdf)

# Resources
IMAGES := $(wildcard images/*.jpg images/*.pdf images/*.png)

.PHONY: all grammar paper submission view-paper view-submission clean abstract

all: ${PDF_SUBMISSION} ${PDF_PAPER}

# spelling and grammar
grammar: $(TEX_MAIN_PAPER)
	# check that textidote exists.
	@textidote --version
	# allowed to fail since it throws error if we have grammar mistakes
	-textidote --check en --output html $< > index.html
	python3 -m http.server

refcheck: paper
	@grep -e 'refcheck.*Unused' paper.log

# Generate the SHA hashes of custom lexers for minted
# NOTE: if any new lexers are added, they ought to be added to the 
#       dependencies here
.latexminted_config: tools/lexers/Lean4Lexer.py tools/lexers/MLIRLexer.py
	./tools/check_latexminted_config_exists.sh
	./tools/generate_lexers_json.py


${PDF_PAPER}: ${TEX_MAIN_PAPER} ${IMAGES} .latexminted_config
	latexmk ${TEX_MAIN_PAPER}

${PDF_SUBMISSION}: ${TEX_MAIN_SUBMISSION} ${IMAGES} .latexminted_config
	latexmk ${TEX_MAIN_SUBMISSION}

abstract: ${TEX_MAIN_PAPER}
	./tools/extract-abstract.py -i $< -o $@.md

paper: ${PDF_PAPER}

submission: ${PDF_SUBMISSION}

view-paper: ${TEX_MAIN_PAPER} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_PAPER}

view-submission: ${TEX_MAIN_SUBMISSION} ${IMAGES}
	latexmk -pvc ${TEX_MAIN_SUBMISSION}

clean:
	latexmk -C
	rm ".latexminted_config"
