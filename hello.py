# Cynthia Cheung
# 111756494
import sys
import ply.lex as lex
import ply.yacc as yacc


class Error(Exception):
    pass


class SbmlError(Error):
    def __init__(self, message):
        self.message = message


# Node
class Node():
    def __init__(self):
        self.parent = None


# Negation node
class Negation(Node):
    def __init__(self, child):
        super().__init__()
        self.child = child
        self.child.parent = self

    def eval(self):
        children = self.child.eval()
        if type(children) is bool:
            return not children
        else:
            raise SbmlError("Semantic Error")


# Conjunction Node
class Conjunction(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if type(leftchild) is bool and type(rightchild) is bool:
            return leftchild and rightchild
        else:
            raise SbmlError("Semantic Error")


# Disjunction node
class Disjunction(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if type(leftchild) is bool and type(rightchild) is bool:
            return leftchild or rightchild
        else:
            raise SbmlError("Semantic Error")


# Tuple
class Tuple(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        tuplelist = []
        for i in self.value:
            tuplelist.append(i.eval())
        tupleval = tuple(tuplelist)
        return tupleval


# Tuple Index
class TupleIndex(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        ind = self.left.eval()
        tup = self.right.eval()
        if ind < 1 or ind > len(tup):
            raise SbmlError("Semantic Error")
        if type(ind) is int:
            return tup[ind - 1]
        else:
            raise SbmlError("Semantic Error")


# List
class List(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        listval = []
        for i in self.value:
            listval.append(i.eval())
        return listval


# List Indexing
class Indexing(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        val = self.left.eval()
        num = self.right.eval()
        if num < 0 or num > (len(val) - 1):
            raise SbmlError("Semantic Error")
        if type(num) is int:
            return val[num]
        else:
            raise SbmlError("Semantic Error")


# Expression
class Expression(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()


# Less
class Less(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if type1 is str and type2 is str:
            return self.left.eval() < self.right.eval()
        elif (type1 is int or type1 is float) and (type2 is int or type2 is float):
            return self.left.eval() < self.right.eval()
        else:
            raise SbmlError("Semantic Error")


# Less Equal
class LessEqual(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if type1 is str and type2 is str:
            return self.left.eval() <= self.right.eval()
        elif (type1 is int or type1 is float) and (type2 is int or type2 is float):
            return self.left.eval() <= self.right.eval()
        else:
            raise SbmlError("Semantic Error")


# Greater
class Greater(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if type1 is str and type2 is str:
            return self.left.eval() > self.right.eval()
        elif (type1 is int or type1 is float) and (type2 is int or type2 is float):
            return self.left.eval() > self.right.eval()
        else:
            raise SbmlError("Semantic Error")


# Greater Equal
class GreaterEqual(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if type1 is str and type2 is str:
            return self.left.eval() >= self.right.eval()
        elif (type1 is int or type1 is float) and (type2 is int or type2 is float):
            return self.left.eval() >= self.right.eval()
        else:
            raise SbmlError("Semantic Error")


# Equals
class Equals(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if type1 is str and type2 is str:
            return self.left.eval() == self.right.eval()
        elif (type1 is int or type1 is float) and (type2 is int or type2 is float):
            return self.left.eval() == self.right.eval()
        else:
            raise SbmlError("Semantic Error")


# Not Equal

class NotEqual(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if type1 is str and type2 is str:
            return self.left.eval() != self.right.eval()
        elif (type1 is int or type1 is float) and (type2 is int or type2 is float):
            return self.left.eval() != self.right.eval()
        else:
            raise SbmlError("Semantic Error")


# Addition
class Addition(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if type(leftchild) is int and (type(rightchild) is int or type(rightchild) is float):
            return leftchild + rightchild
        elif type(leftchild) is float and (type(rightchild) is int or type(rightchild) is float):
            return leftchild + rightchild
        elif type(leftchild) is str and type(rightchild) is str:
            return leftchild + rightchild
        elif type(leftchild) is list and type(rightchild) is list:
            return leftchild + rightchild
        else:
            raise SbmlError("Semantic Error")
# Subtraction
class Subtraction(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if type(leftchild) is int and (type(rightchild) is int or type(rightchild) is float):
            return leftchild - rightchild
        elif type(leftchild) is float and (type(rightchild) is int or type(rightchild) is float):
            return leftchild - rightchild
        else:
            raise SbmlError("Semantic Error")

# Multiply
class Multiply(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if type(leftchild) is int and (type(rightchild) is int or type(rightchild) is float):
            return leftchild * rightchild
        elif type(leftchild) is float and (type(rightchild) is int or type(rightchild) is float):
            return leftchild * rightchild
        else:
            raise SbmlError("Semantic Error")

# Division
class Division(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if rightchild == 0:
            raise SbmlError("Semantic Error")
        if type(leftchild) is int and (type(rightchild) is int or type(rightchild) is float):
            return leftchild / rightchild
        elif type(leftchild) is float and (type(rightchild) is int or type(rightchild) is float):
            return leftchild / rightchild
        else:
            raise SbmlError("Semantic Error")


# Integer Division
class Intdiv(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if rightchild == 0:
            raise SbmlError("Semantic Error")
        if type(leftchild) is int and type(rightchild) is int:
            return leftchild // rightchild
        else:
            raise SbmlError("Semantic Error")

# Mod
class Mod(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if type(leftchild) is int and type(rightchild) is int:
            return leftchild % rightchild
        else:
            raise SbmlError("Semantic Error")

# Exponent
class Exponent(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        rightchild = self.right.eval()
        if type(leftchild) is int and (type(rightchild) is int or type(rightchild) is float):
            return leftchild ** rightchild
        elif type(leftchild) is float and (type(rightchild) is int or type(rightchild) is float):
            return leftchild ** rightchild
        else:
            raise SbmlError("Semantic Error")

# Con
class Cons(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        conlist = self.right.eval()
        if type(conlist) is not list:
            raise SbmlError("Semantic Error")
        else:
            conlist.insert(0, self.left.eval())
            return conlist

# Membership
class Member(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        leftchild = self.left.eval()
        memberlist = self.right.eval()
        if type(leftchild) is str and type(memberlist) is str:
            return leftchild in memberlist
        elif type(memberlist) is list:
            return self.left.eval() in memberlist
        else:
            raise SbmlError("Semantic Error")

# Uminus
class Uminus(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        val = self.value.eval()
        if type(val) is int or type(val) is float:
            return self.value.eval() * -1
        else:
            raise SbmlError("Semantic Error")

# Print
class Print(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        print(self.value.eval())

# Block
class Block(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        blocklist = self.value
        for i in blocklist:
            i.eval()
            # print(i.eval())

# If node
class If(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        express = self.left.eval()
        if type(express) is not bool:
            raise SbmlError("Semantic Error")
        if express is True:
            body = self.right.eval()
            return body
        else:
            return False

# If Else
class If_Else(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        ifstatement = self.left.eval()
        if ifstatement is False:
            elsestatement = self.right.eval()
            return elsestatement
        else:
            return ifstatement

# While loop
class While(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        whileexpress = self.left
        whileblock = self.right
        while whileexpress.eval() is True:
            whileblock.eval()
        # No longer true
        return None


# Assign Node
class Assign(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        # self.left.parent = self
        self.right.parent = self

    def eval(self):
        var = self.left
        val = self.right.eval()
        variableTable[var] = val
        return variableTable[var]

# Assign Index, indicies in list
class AssignIndex(Node):
    def __init__(self, value, index, assignment):
        super().__init__()
        self.value = value
        self.left = index
        self.right = assignment

    def getindex(self, variable, index, assigned):
        # Only 1 index
        if len(index) == 1:
            i = index[0].eval()
            if type(i) is not int:
                raise SbmlError("Semantic Error")
            elif i < 0 or i > (len(variable) - 1):
                raise SbmlError("Semantic Error")
            elif type(variable) is not list:
                    raise SbmlError("Semantic Error")
            else:
                variable[i] = assigned #update that value
        else:
            indexs = index[1:] # rest of the list
            j = indexs[0].eval()
            if type(j) is not int:
                raise SbmlError("Semantic Error")
            elif j < 0 or j > (len(variable) - 1):
                raise SbmlError("Semantic Error")
            else:
                self.getindex(variable[j], indexs, assigned)

    def eval(self):
        var = self.value
        ind = self.left
        assigned = self.right.eval()
        variable = variableTable[var]
        if type(variable) is not list:
            raise SbmlError("Semantic Error")
        else:
            self.getindex(variable, ind, assigned) #update that index
            variableTable[var] = variable

# True
class AST_True(Node):
    def __init__(self):
        super().__init__()
        self.value = True

    def eval(self):
        return self.value


# False
class AST_False(Node):
    def __init__(self):
        super().__init__()
        self.value = False

    def eval(self):
        return self.value


# Integer
class INTEGER(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value


# Real
class REAL(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value


# String
class String(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value

# Variable
class Variable(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        var = self.value
        if var in variableTable:
            return variableTable[var]
        else:
            raise SbmlError("Semantic Error")


reserved = {
    'True': 'TRUE',
    'andalso': 'CONJUNCTION',
    'orelse': 'DISJUNCTION',
    'False': 'FALSE',
    'div': 'INTEGER_DIV',
    'mod': 'MOD',
    'in': 'IN',
    'not': 'NEGATION',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

# Tokens

tokens = ('INTEGER',
          'REAL',
          'STRING',
          'LEFT_BRACKET',
          'RIGHT_BRACKET',
          'LEFT_PARENTHESIS',
          'RIGHT_PARENTHESIS',
          'COMMA',
          'TUPLE_IND',
          'MULTIPLY',
          'EXPONENT',
          'DIVIDE',
          'PLUS',
          'MINUS',
          'CON',
          'LESS',
          'LESS_EQUAL',
          'EQUALS',
          'NOT_EQUAL',
          'GREATER_EQUAL',
          'GREATER',
          'SEMICOLON',
          'ASSIGN',
          'VARIABLE',
          'LCURLY',
          'RCURLY'
          ) + tuple(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_EXPONENT = r'\*\*'
t_COMMA = r','
t_LESS = r'<'
t_LESS_EQUAL = r'<='
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_EQUALS = r'=='
t_NOT_EQUAL = r'<>'
t_TUPLE_IND = r'\#'
t_CON = r'\:\:'
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_LCURLY = r'\{'
t_RCURLY = r'\}'


# Check for reserved words else it's a variable
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_REAL(t):
    r'((\d*\.\d+)|(\d+\.\d*))(e-?\d+)?'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'(\" [^"]* \") | (\' [^\']* \')'
    t.value = t.value[1:-1]
    return t


# New line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Ignore
t_ignore = ' \t'


# Error
def t_error(t):
    raise SbmlError("Syntax Error")


lexer = lex.lex()


def tokenize(inp):
    lexer.input(inp)
    while True:
        tok = lexer.token()
        if not tok:
            break
        # print(tok)


# Parsing
variableTable = {}

precedence = (
    ('left', 'DISJUNCTION'),
    ('left', 'CONJUNCTION'),
    ('left', 'NEGATION'),
    ('left', 'LESS', 'LESS_EQUAL', 'EQUALS', 'NOT_EQUAL', 'GREATER_EQUAL', 'GREATER'),
    ('right', 'CON'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'INTEGER_DIV', 'MOD'),
    ('right', 'EXPONENT'),
    ('left', 'LEFT_BRACKET', 'RIGHT_BRACKET'),
    ('left', 'TUPLE_IND'),
    ('left', 'COMMA'),
    ('left', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS'),
    ('right', 'UMINUS')
)

def p_start(p):
    'start : block'
    p[0] = p[1]

def p_prop_conjunction(p):
    'prop : prop CONJUNCTION prop'
    p[0] = Conjunction(p[1], p[3])


def p_prop_disjunction(p):
    'prop : prop DISJUNCTION prop'
    p[0] = Disjunction(p[1], p[3])


def p_prop_negation(p):
    'prop : NEGATION prop'
    p[0] = Negation(p[2])


def p_prop_true(p):
    'prop : TRUE'
    p[0] = AST_True()


def p_prop_false(p):
    'prop : FALSE'
    p[0] = AST_False()


def p_prop_list_index(p):
    'prop : prop index'
    p[0] = Indexing(p[1], p[2])


def p_prop_index(p):
    'index : LEFT_BRACKET prop RIGHT_BRACKET'
    p[0] = p[2]


def p_list(p):
    'prop : list'
    p[0] = p[1]


def p_prop_list(p):
    '''list : LEFT_BRACKET expression RIGHT_BRACKET
            | LEFT_BRACKET RIGHT_BRACKET '''
    if len(p) == 3:
        p[0] = List([])
    else:
        p[0] = List(p[2])


def p_prop_expression(p):
    '''expression : value COMMA expression
                | value '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1] + p[3])


def p_prop_value(p):
    'value : prop'
    p[0] = [p[1]]


def p_prop_tupleindex(p):
    'prop : TUPLE_IND Number prop'
    p[0] = TupleIndex(p[2], p[3])


def p_prop_tuple(p):
    'prop : LEFT_PARENTHESIS express RIGHT_PARENTHESIS'
    p[0] = Tuple(p[2])


def p_prop_tuple_exp(p):
    '''express : element COMMA expression
                | element COMMA'''
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = (p[1] + p[3])


def p_prop_tuple_value(p):
    'element : prop'
    p[0] = [p[1]]


def p_prop_express(p):
    'prop : LEFT_PARENTHESIS prop RIGHT_PARENTHESIS'
    p[0] = Expression(p[2])


def p_prop_less(p):
    'prop : prop LESS prop'
    p[0] = Less(p[1], p[3])


def p_prop_lessEqual(p):
    'prop : prop LESS_EQUAL prop'
    p[0] = LessEqual(p[1], p[3])


def p_prop_Greater(p):
    'prop : prop GREATER prop'
    p[0] = Greater(p[1], p[3])


def p_prop_GreaterEqual(p):
    'prop : prop GREATER_EQUAL prop'
    p[0] = GreaterEqual(p[1], p[3])


def p_prop_Equals(p):
    'prop : prop EQUALS prop'
    p[0] = Equals(p[1], p[3])


def p_prop_NotEqual(p):
    'prop : prop NOT_EQUAL prop'
    p[0] = NotEqual(p[1], p[3])

def p_prop_addition(p):
    'prop : prop PLUS prop'
    p[0] = Addition(p[1], p[3])


def p_prop_subtraction(p):
    'prop : prop MINUS prop'
    p[0] = Subtraction(p[1], p[3])


def p_prop_multiply(p):
    'prop : prop MULTIPLY prop'
    p[0] = Multiply(p[1], p[3])


def p_prop_division(p):
    'prop : prop DIVIDE prop'
    p[0] = Division(p[1], p[3])


def p_prop_intdiv(p):
    'prop : prop INTEGER_DIV prop'
    p[0] = Intdiv(p[1], p[3])


def p_prop_mod(p):
    'prop : prop MOD prop'
    p[0] = Mod(p[1], p[3])


def p_prop_exponent(p):
    'prop : prop EXPONENT prop'
    p[0] = Exponent(p[1], p[3])

def p_prop_cons(p):
    'prop : prop CON prop'
    p[0] = Cons(p[1], p[3])


def p_prop_member(p):
    'prop : prop IN prop'
    p[0] = Member(p[1], p[3])

def p_expression_uminus(p):
    'prop : MINUS prop %prec UMINUS'
    p[0] = Uminus(p[2])

def p_block(p):
    '''block : LCURLY statement_list RCURLY
            | LCURLY RCURLY '''
    if len(p) == 3:
        p[0] = Block([])
    else:
        p[0] = Block(p[2])


def p_statementlist(p):
    '''statement_list : statement_list statement
                    | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_statement(p):
    '''statement : print_statement
                | if_else_statement
                | while_statement
                | assignment_statement
                | if_statement
                | block'''

    p[0] = p[1]

def p_prop_if_statement(p):
    'if_statement : IF LEFT_PARENTHESIS prop RIGHT_PARENTHESIS block'
    p[0] = If(p[3], p[5])

def p_prop_if_else_statement(p):
    'if_else_statement : if_statement ELSE block'
    p[0] = If_Else(p[1], p[3])

def p_prop_print(p):
    'print_statement : PRINT LEFT_PARENTHESIS prop RIGHT_PARENTHESIS SEMICOLON'
    p[0] = Print(p[3])

def p_prop_while_statement(p):
    'while_statement : WHILE LEFT_PARENTHESIS prop RIGHT_PARENTHESIS block'
    p[0] = While(p[3], p[5])

def p_assignment_statement(p):
    '''assignment_statement : VARIABLE ASSIGN prop SEMICOLON
                            | VARIABLE indexes ASSIGN prop SEMICOLON'''
    if len(p) == 5:
        p[0] = Assign(p[1], p[3])
    else:
        p[0] = AssignIndex(p[1], p[2], p[4])

def p_index_list(p):
    '''indexes : index
               | index indexes'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_number(p):
    'prop : Number'
    p[0] = p[1]


def p_prop_integer(p):
    'Number : INTEGER'
    p[0] = INTEGER(p[1])


def p_prop_real(p):
    'Number : REAL'
    p[0] = REAL(p[1])


def p_prop_String(p):
    'prop : STRING'
    p[0] = String(p[1])

def p_prop_variable(p):
    'prop : VARIABLE'
    p[0] = Variable(p[1])

def p_error(p):
    raise SbmlError("Syntax Error")


parser = yacc.yacc()


def parse(inp):
    result = parser.parse(inp)
    return result


def main():
    try:
        filename = sys.argv[1]
        f = open(filename, 'r')
        fline = f.read()
        result = parse(fline)
        # print(result)
        if result is not None:
            result.eval()
            #print("Evaluation:", result.eval())
    except SbmlError as e:
        print(e)


if __name__ == "__main__":
    main()
