#!/bin/bash
for file in *.aux ; 
	do
		bibtex ‘phdThesis $file.aux‘
done