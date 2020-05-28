# SBML
sbml is a hybrid programming language that combines the features found in Python and SML.  It is written in PLY (Python Lex and Yacc)

#How To Run
Need:
Python 3
PLY

On the command line run:
python sbml.py <input_filename>
The input_filename will hold the input program.  This input program can contain multiple function definitions followed by one executed main block.
The source code will take the input file and parse the input expression.  Semantic analysis and expression evaluation are done through recursive
operation on the content.
