##################################################################
# Makefile for LaTeX
##################################################################
# Use:
# make
# make clean
TEX:=$(shell ls *.tex)
FILES = *.tex Makefile *.bst *.pdf *.bib
FOLDER = PhdThesis/
TEXLIST = TexList.txt
FIGLIST = FigList.txt
OTHER = *~ *.aux *.dvi *.toc *.bbl *.blg *.out *.thm *.ps *.idx *.ilg *.ind *.tdo *.pdf *.tar.gz *.log *.spl *.synctex.gz
NAMETAR1:= $(shell date '+%Y%b%d_%H_%M')
NAMETAR = "$(NAMETAR1)_phdThesis.tar.gz"
NAMETARTEX = "$(NAMETAR1)_phdThesisTex.tar.gz"
NAMETARFIG = "$(NAMETAR1)_phdThesisFig.tar.gz"
pdflatex: phdThesis.tex
	pdflatex --synctex=1 phdThesis.tex
	#bibtex papers/paperA/paperA
	#bibtex papers/paperB/paperB
	bibtex phdThesis.aux
	pdflatex --synctex=1 phdThesis.tex
	pdflatex --synctex=1 phdThesis.tex
	#rm -f $(OTHER) $(PS)
	#(cd introduction && rm -f $(OTHER) $(PS))
	#(cd papers/* && rm -f $(OTHER) $(PS))
clean:
	rm -f $(OTHER) $(PS)
	(cd introduction && rm -f $(OTHER) $(PS))
	(cd papers/* && rm -f $(OTHER) $(PS))
#
tar:
	(cd ..&& tar -cvf $(NAMETAR) $(FOLDER))
#
tarFig:
	(cd ..&& tar -cvf $(NAMETARFIG) -T $(FIGLIST))
	
#
tarTex:
	(cd ..&& tar -cvf $(NAMETARTEX) -T $(TEXLIST))
	
ch3:	Chapter3.tex
	pdflatex --synctex=1 Chapter3.tex
	bibtex Chapter3.aux
	pdflatex --synctex=1 Chapter3.tex
	pdflatex --synctex=1 Chapter3.tex

ch4:	Chapter4.tex
	pdflatex --synctex=1 Chapter4.tex
	bibtex Chapter4.aux
	pdflatex --synctex=1 Chapter4.tex
	pdflatex --synctex=1 Chapter4.tex

ch5:	Chapter5.tex
	pdflatex --synctex=1 Chapter5.tex
	bibtex Chapter5.aux
	pdflatex --synctex=1 Chapter5.tex
	pdflatex --synctex=1 Chapter5.tex

Chori:	Chorizo.sh
	sh Chorizo.sh
	pdflatex --synctex=1 StrongConvergenceLSMethod.tex
	pdflatex --synctex=1 StrongConvergenceLSMethod.tex