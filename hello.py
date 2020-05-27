# Cynthia Cheung
# 111756494
import sys
import ply.lex as lex
import ply.yacc as yacc


# Node class from class
class Node():
    def __init__(self):
        self.parent = None

    def parentCount(self):
        count = 0
        current = self.parent
        while current is not None:
            count += 1
            current = current.parent
        return count

# Negation node from class
class Negation(Node):
    def __init__(self, child):
        super().__init__()
        self.child = child
        self.child.parent = self

    def eval(self):
        return not self.child.eval()



# Conjuction node
class Conjunction(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        return self.left.eval() and self.right.eval()


# Disjunction node
class Disjunction(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        return self.left.eval() or self.right.eval()




class Addition(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() + self.right.eval()




class Subtraction(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if (type2 != int and type2 != float) and (type1 != int and type1 != float):
            print("Syntax Error")
            return
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() - self.right.eval()




class Multiply(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if (type2 != int and type2 != float) and (type1 != int and type1 != float):
            print("Syntax Error")
            return
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() * self.right.eval()




class Division(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if (type2 != int and type2 != float) and (type1 != int and type1 != float):
            print("Syntax Error")
            return
        if type1 != type2:
            print("Semantic Error")
            return
        elif self.right.eval() == 0:
            print("Semantic Error")
            return
        else:
            return self.left.eval() / self.right.eval()




class Intdiv(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if (type2 != int and type2 != float) and (type1 != int and type1 != float):
            print("Syntax Error")
            return
        if type1 != type2:
            print("Semantic Error")
            return
        elif self.right.eval() == 0:
            print("Semantic Error")
            return
        else:
            return self.left.eval() // self.right.eval()



class Mod(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if (type2 != int and type2 != float) and (type1 != int and type1 != float):
            print("Syntax Error")
            return
        if type1 != type2:
            print("Semantic Error")
            return
        elif self.right.eval() == 0:
            print("Semantic Error")
            return
        else:
            return self.left.eval() % self.right.eval()




class Exponent(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        type1 = type(self.left.eval())
        type2 = type(self.right.eval())
        if (type2 != int and type2 != float) and (type1 != int and type1 != float):
            print("Syntax Error")
            return
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() ** self.right.eval()



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
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() < self.right.eval()



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
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() <= self.right.eval()




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
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() > self.right.eval()



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
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() >= self.right.eval()




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
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() == self.right.eval()



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
        if type1 != type2:
            print("Semantic Error")
            return
        else:
            return self.left.eval() != self.right.eval()




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
            print("Semantic Error")
            return
        try:
            isinstance(num, int)
            return val[num]
        except:
            print("Syntax Error")
            return


class Cons(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        conlist = self.right.eval()
        conlist.insert(0, self.left.eval())
        return conlist




class Member(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        memberlist = self.right.eval()
        return self.left.eval() in memberlist



class List(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        listval = []
        for i in self.value:
            listval.append(i.eval())
        return listval


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
            print("Semantic Error")
            return
        try:
            isinstance(ind, int)
            return tup[ind - 1]
        except:
            print("Syntax Error")
            return




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


class Expression(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()


class AST_True(Node):
    def __init__(self):
        super().__init__()
        self.value = True

    def eval(self):
        return self.value


class AST_False(Node):
    def __init__(self):
        super().__init__()
        self.value = False

    def eval(self):
        return self.value

class Uminus(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval() * -1



class INTEGER(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value



class REAL(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value



class String(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value



reserved = {
    'True': 'TRUE',
    'andalso': 'CONJUNCTION',
    'orelse': 'DISJUNCTION',
    'False': 'FALSE',
    'div': 'INTEGER_DIV',
    'mod': 'MOD',
    'in': 'IN',
    'not': 'NEGATION'
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
          'GREATER'
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


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
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
    print("Illegal Character '%s', at %d, %d" % (t.value[0], t.lineno, t.lexpos))
    t.lexer.skip(1)


lexer = lex.lex()


def tokenize(inp):
    lexer.input(inp)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


# Parsing
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

def p_expression_uminus(p):
    'prop : MINUS prop %prec UMINUS'
    p[0] = Uminus(p[2])

def p_prop_negation(p):
    'prop : NEGATION boolean'
    p[0] = Negation(p[2])


def p_prop_conjunction(p):
    'prop : boolean CONJUNCTION boolean'
    p[0] = Conjunction(p[1], p[3])


def p_prop_disjunction(p):
    'prop : boolean DISJUNCTION boolean'
    p[0] = Disjunction(p[1], p[3])


def p_prop_cons(p):
    'prop : prop CON prop'
    p[0] = Cons(p[1], p[3])


def p_prop_member(p):
    'prop : prop IN prop'
    p[0] = Member(p[1], p[3])


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


def p_prop_express(p):
    'prop : LEFT_PARENTHESIS prop RIGHT_PARENTHESIS'
    p[0] = Expression(p[2])


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


def p_prop_String(p):
    'prop : STRING'
    p[0] = String(p[1])


def p_number(p):
    'prop : Number'
    p[0] = p[1]


def p_prop_real(p):
    'Number : REAL'
    p[0] = REAL(p[1])


def p_prop_integer(p):
    'Number : INTEGER'
    p[0] = INTEGER(p[1])


def p_prop_boolean(p):
    'prop : boolean'
    p[0] = p[1]


def p_prop_true(p):
    'boolean : TRUE'
    p[0] = AST_True()


def p_prop_false(p):
    'boolean : FALSE'
    p[0] = AST_False()


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()


def parse(inp):
    result = parser.parse(inp)
    return result



def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    fline = f.readlines()
    for p in fline:
        print("Input: ")
        print(p)
        # tokenize(inp)
        result = parse(p)
        #print(result)
        if result is not None:
            print("Evaluation:", result.eval())


if __name__ == "__main__":
    main()
