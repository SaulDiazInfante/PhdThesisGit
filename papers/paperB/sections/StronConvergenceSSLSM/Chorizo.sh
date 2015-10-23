cat Preamble.tex > StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' 
echo '%              Section 1\n'
echo '%********************************************************************************************\n'
echo '\section{Introduction} \n' >> StrongConvergenceLSMethod.tex
cat  Introduction.tex  >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' 
echo '%              Section 2\n'
echo '%********************************************************************************************\n'
echo '\section{Existence and uniqueness of the solution} \n' >> StrongConvergenceLSMethod.tex
cat  ExistenceAndUniqueness.tex >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' 
echo '%              Section 3\n'
echo '%********************************************************************************************\n'
echo '\section{Construction of the Linear Steklov method} \n' >> StrongConvergenceLSMethod.tex
cat  sssmConstruction.tex >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' 
echo '%              Section 4\n'
echo '%********************************************************************************************\n'
echo '\section{Strong Convergecne using the Higham-Mao-Stuart technique} \n' >> StrongConvergenceLSMethod.tex
cat  HighamConvergenceTechnique.tex  >> StrongConvergenceLSMethod.tex
echo '%********************************************************************************************\n' 
echo '%              Section 5\n'
echo '%********************************************************************************************\n'
echo '\section{Strong Convergence of the Linear Steklov Method} \n' >> StrongConvergenceLSMethod.tex
cat  StrongConevergenceProof.tex >> StrongConvergenceLSMethod.tex
cat  BackMater.tex AuxiliarResults.tex >> StrongConvergenceLSMethod.tex
echo '\end{appendices}' >> StrongConvergenceLSMethod.tex
echo '\end{document}' >> StrongConvergenceLSMethod.tex  