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
| Tuple | Finite, ordered sequence of elements separated by commas and enclosed within matching parentheses. Elements of the tuple need not be of the same type.  | #3(4, 3, 2, 1) |

# SBML Literal Description
Integer: Positive (no sign) or negative (unary -) whole numbers in base-10 representation (decimal representation). An integer literal is one or more digits, 0-9. <br />

Real: A real value is represented by 0 or more digits (0-9), followed by a decimal point, ".", followed by 0 or more digits (0-9), except that a decimal point by itself with no leading or trailing digit is not a real. A real can also contain exponents as in scientific  notation. In this case, a real value, as defined above, is followed by an "e" character and then a positive or negative integer, as defined above. <br />

Boolean: True, False <br />

String: A string literal begins with a single or double quote, followed by zero or more non-quote characters, and ends with a matching quote. The value of the string literal does not include the starting and ending quotes. <br />

List: A list literal is composed by a left square bracket, followed by a comma-separated sequence of zero or more expressions, followed by a right square bracket.

# Operators
| Operator | Description |
| --- | --- |
|  ( expression ) | A parenthesized expression |
|  ( expression1, expression2, … ) | Tuple constructor. A singleton tuple can be constructed by including a comma after the expression. |
|  #i(tuple) | returns the argument at index i in the tuple. Indices start at 1. |
| a[b] | Indexing Operation. b can be any expression. |
|  a ** b | Exponentiation. base a raised to the power b. |
|  a * b | Multiplication. Overloaded for integers and reals. |
|  a / b | Division. Overloaded for integers and reals, but result is always a real value. |
|  a div b  | Integer Division. Returns just the quotient. a and b are integers. |
|  a mod b | Divides a by b and returns just the remainder. a and b are integers. |
|  a + b | Addition. Overloaded for integers, reals, strings, and lists. |
|  a – b |  Subtraction. Overloaded for integers and reals. |
|  a in b | Membership. Evaluates to True if it finds the value of a inside the string or list represented by b. |
|  a::b  | Cons. Adds operand a to the front of the list referred to by operand b. |
|  not a | Boolean negation. |
|  a andalso b  |  Boolean Conjunction (AND) |
|  a orelse b  |  Boolean Disjunction (OR) |
|  a < b |  Less than. Comparison. |
|  a <= b  | Less than or equal to. Comparison. |
|   a == b  | Equal to. Comparison. |
|  a <> b  |  Not equal to. Comparison. |
|  a >= b  |  Greater than or equal to. Comparison. |
|  a > b  | Greater than. Comparison. |
