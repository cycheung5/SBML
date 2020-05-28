# SBML
sbml is a hybrid programming language that combines the features found in Python and SML.  It is written in PLY (Python Lex and Yacc)

# How To Run
Need: <br />
Python 3 <br />
PLY

On the command line: <br />
python sbml.py <input_filename>

The input_filename will hold the input program.  This input program can contain multiple function definitions followed by one executed main block.
The source code will take the input file and parse the input expression.  Semantic analysis and expression evaluation are done through recursive
operation on the content.

# SBML Datatypes:
| Datatype | Description |
| --- | --- |
| Numbers | Integers and Reals |
| Boolean | True and False |
| Strings | Sequences of characters enclosed within matching single or double quotes in a single line. |
| List |  Finite, ordered sequence of elements separated by commas and enclosed within matching square brackets. Elements of the list need not be of the same type. |
| Tuple | Finite, ordered sequence of elements separated by commas and enclosed within matching parentheses. Elements of the tuple need not be of the same type.  |
