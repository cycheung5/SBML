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

# Operator Precedence (Lowest to Highest)
All operators are left-associative, except for exponentiation  (** ) and cons (::), which are right-associative.  Operators on the same line have the same precedence.

orelse Boolean Disjunction <br />
andalso Boolean Conjunction <br />
not Boolean Negation <br />
 <, <=, ==, <>, >=, > Comparison Operators (for  numbers and strings) <br />
 h::t Cons operator <br />
 in Membership test <br />
 +, - Addition and Subtraction  (Overloaded for numbers, strings, lists) <br />
 \*, /, div, mod Multiplication, Division, Integer Division, Modulus ** Exponentiation <br />
 a[b] Indexing <br />
 #i(tuple) Tuple Indexing. (exp1, exp2,...) Tuple Creation <br />
 (exp) Parenthetical Expression

# Operator Semantics

 Indexing: Operand a must be either a string or a list.  Operand b must be an integer. If a is a string,  then return the b-th character as a string. If a is a list, then return the b-th element as an instance of whatever type it is. The index is 0-based. If the index is out of bounds, then this is a semantic error.

 Addition: Operands must either both be numbers, or both be strings, or both be lists. If they are integers or reals, then addition with standard (Python)
  semantics is performed. If a and b are both strings, then string concatenation is performed. If a and b are both lists, then list concatenation is performed.

 Subtraction: Operands must both be integers or reals. Performed using standard subtraction semantics.

 Multiplication: Operands must both be integers or reals. Performed using standard multiplication semantics.

 Division: Operands must both be integers or reals. Operand b cannot be 0. Performed using standard division semantics.

 Booleans: Operands for Boolean operations (not, andalso, orelse) must be Boolean values.

 Comparisons: Operands must either both be numbers or both be strings. Comparison of numbers (integers and strings) should follow standard semantics. Comparison of strings should return True if comparison is true and False if comparison is False.


# Variables and Assignment

Variable names begin with an ASCII character, which may be followed by zero or more ASCII characters, digits, or underscores. <br />
Support for assignment to variables are included such as "x = 1;" and assignment to index list values such as "array = [1,2,3];" .  Variables can also be used in expressions.  For instance, if x is assigned to 1, then "print(x);" will print 1.

If the variable has had a value assigned to it and the variable is evaluated, then the value is returned.  Otherwise, a "Semantic Error" is thrown and the program exits.  When an indexed list variable is used in an expression, then both the list and the index are evaluated to their value, and
 then the indexed list expression is evaluated. If the variable is not a list (or a string), or the index is not an integer, then a Semantic Error is thrown. If the index is outside the bounds of the list, then a Semantic Error is thrown.

# Statement Types

 Block: A block statement consists of zero or more statements enclosed in curly-braces, "{…}". When the block executes, each of the statements is executed in sequential order.

Assignment: an assignment statement consists of an expression, an equals sign, an expression, and a semicolon, "exp1 = exp2;". When the assignment statement executes the lefthand side expression is assigned the value evaluated for the right-hand side expression.

Print: a print statement consists of the "print" keyword, a left parenthesis, an expression, a right parenthesis, and then a semicolon. When the statement executes, the expression is evaluated for its value. The output displayed should be the same as that produced by Python for that value.

Conditional Statements: <br />
A. If Statements: Consist of a keyword "if", a left parenthesis, an expression, a right parenthesis, and a block statement as the <br />
body of the If statement. When the If statement executes, if the expression evaluates to True, then the block statement composing the body is executed. <br />
B. If-Else Statements: Consist of a keyword "if", a left parenthesis, an expression, a right parenthesis, a block statement as the body of the If clause, the <br />
keyword "else", and a block statement as the body of the Else clause. When the IF-Else statement executes, if the expression is True, then execute the block statement that is the body of the If clause. Otherwise, execute the block statement that is the body of the Else clause.

 Loop Statements: <br />
A. While Loops: A While statement consists of the keyword "while", a left parenthesis, an expression, a right parenthesis, and a block statement that is the body <br />
of  the While statement. Executing the while statement begins by evaluating the condition expression for its value. If the expression evaluates to False, then <br />
 the  While statement terminates. Otherwise, execute the block of statements that compose the body of the While statement, and then repeat the execution of the <br />
 While  statement from the evaluation of the condition expression.
