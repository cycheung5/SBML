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
| Datatype | Description | Example |
| --- | --- | --- |
| Numbers | Integers and Reals | 57, -18, 235, 3.14159, 0.7, .892, 32787, 6.02e-23, 17.0e4 |
| Boolean | True and False | True, False |
| Strings | Sequences of characters enclosed within matching single or double quotes in a single line. |  "Hello World!", "867-5309" |
| List |  Finite, ordered sequence of elements separated by commas and enclosed within matching square brackets. Elements of the list need not be of the same type. | ["a", "b"], [1, 2], [307, "307", 304+3]  |
| Tuple | Finite, ordered sequence of elements separated by commas and enclosed within matching parentheses. Elements of the tuple need not be of the same type.  | Description |




    
