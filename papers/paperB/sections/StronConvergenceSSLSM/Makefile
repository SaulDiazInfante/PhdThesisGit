SOURCE = StrongConvergenceOfSSLSM
FILES= *.tex Makefile *.bst *.pdf *.bib
make:
	pdflatex -synctex=1 -interaction=nonstopmode $(SOURCE).tex
	bibtex $(SOURCE).aux
	pdflatex -synctex=1 -interaction=nonstopmode $(SOURCE).tex
	pdflatex -synctex=1 -interaction=nonstopmode $(SOURCE).tex
	make clean

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.out *.glo *.glg *.gls *.ist *.xdy *.1 *.toc *.snm *.nav *.vrb *.fls *.fdb_latexmk *.pyg

tar: $(FILES)
	tar -cvf MultidimensionalSteklov.tar $(FILES)
