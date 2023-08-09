scales.pdf : scales.tex raw.tex
	pdflatex scales.tex > /dev/null
raw.tex : make.py scales.csv
	./make.py > raw.tex
