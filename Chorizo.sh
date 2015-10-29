cat ./papers/paperB/sections/StronConvergenceSSLSM/Preamble.tex > StrongConvergenceLSMethod.tex
echo '\n%********************************************************************************************'  >> StrongConvergenceLSMethod.tex 
echo '%              Section 1' >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' >> StrongConvergenceLSMethod.tex
echo '\section{Introduction} \n' >> StrongConvergenceLSMethod.tex
cat  ./papers/paperB/sections/StronConvergenceSSLSM/Introduction.tex  >> StrongConvergenceLSMethod.tex
echo '\n%********************************************************************************************'  >> StrongConvergenceLSMethod.tex 
echo '%              Sectison 2' >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' >> StrongConvergenceLSMethod.tex
echo '\section{Existence and uniqueness of the solution} \n' >> StrongConvergenceLSMethod.tex
cat  ./papers/paperB/sections/StronConvergenceSSLSM/ExistenceAndUniqueness.tex >> StrongConvergenceLSMethod.tex
echo '\n%********************************************************************************************'  >> StrongConvergenceLSMethod.tex 
echo '%              Section 3' >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' >> StrongConvergenceLSMethod.tex
echo '\section{Construction of the Linear Steklov method} \n' >> StrongConvergenceLSMethod.tex
cat  ./papers/paperB/sections/StronConvergenceSSLSM/sssmConstruction.tex >> StrongConvergenceLSMethod.tex
echo '\n%********************************************************************************************'  >> StrongConvergenceLSMethod.tex 
echo '%              Section 4' >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' >> StrongConvergenceLSMethod.tex
echo '\section{Strong Convergecne using the Higham-Mao-Stuart technique} \n' >> StrongConvergenceLSMethod.tex
cat  ./papers/paperB/sections/StronConvergenceSSLSM/HighamConvergenceTechnique.tex  >> StrongConvergenceLSMethod.tex
echo '\n%********************************************************************************************'  >> StrongConvergenceLSMethod.tex 
echo '%              Section 5' >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' >> StrongConvergenceLSMethod.tex
echo '\section{Strong Convergence of the Linear Steklov Method} \n' >> StrongConvergenceLSMethod.tex
cat  ./papers/paperB/sections/StronConvergenceSSLSM/StrongConevergenceProof.tex >> StrongConvergenceLSMethod.tex
echo '\n%********************************************************************************************'  >> StrongConvergenceLSMethod.tex 
echo '%              Section 6' >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' >> StrongConvergenceLSMethod.tex
echo '\section{Convergence Rate} \n' >> StrongConvergenceLSMethod.tex
cat ./papers/paperB/sections/StronConvergenceSSLSM/ConvergenceRates.tex >> StrongConvergenceLSMethod.tex
echo '\n%********************************************************************************************'  >> StrongConvergenceLSMethod.tex 
echo '%\t\t\t\t Bibliography' >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' >> StrongConvergenceLSMethod.tex
#
cat ./papers/paperB/sections/StronConvergenceSSLSM/BackMater.tex >> StrongConvergenceLSMethod.tex
cat ./papers/paperB/sections/StronConvergenceSSLSM/AuxiliarResults.tex >> StrongConvergenceLSMethod.tex
echo '\end{appendices}' >> StrongConvergenceLSMethod.tex
echo '\end{document}' >> StrongConvergenceLSMethod.tex
pdflatex StrongConvergenceLSMethod.tex
pdflatex StrongConvergenceLSMethod.tex