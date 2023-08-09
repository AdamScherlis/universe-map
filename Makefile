envelope.pdf : envelope.tex raw.tex
	pdflatex envelope.tex > /dev/null
raw.tex : make.py imgs.csv pts.csv lines.csv
	./make.py > raw.tex
