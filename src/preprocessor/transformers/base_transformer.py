from collections import namedtuple
from lark import Transformer, v_args


class BaseTransformer(Transformer):
    CNAME = str
    STRING = str
    LONG_STRING = str
    NUMBER = str
    true = lambda self, _: 'True'
    false = lambda self, _: 'False'
    none = lambda self, _: 'None'
    COMP_OPERATOR = str

    def identifier(self, items):
        return ''.join(items)

    @v_args(inline=True)
    def inner_name(self, n):
        return '.' + str(n)

    @v_args(inline=True)
    def index(self, number):
        # (number,) = number   без @v_args(inline=True)
        return '[' + str(number) + ']'

    @v_args(inline=True)
    def string(self, st):
        return str(st)

    @v_args(inline=True)
    def expression(self, expr):
        return str(expr)

    @v_args(inline=True)
    def math(self, m):
        return str(m)

    @v_args(inline=True)
    def sum(self, left, right):
        return left + ' + ' + right

    @v_args(inline=True)
    def subtraction(self, left, right):
        return left + ' - ' + right

    @v_args(inline=True)
    def product(self, prod):
        return str(prod)

    @v_args(inline=True)
    def multiplication(self, left, right):
        return left + ' * ' + right

    @v_args(inline=True)
    def division(self, left, right):
        return left + ' / ' + right

    @v_args(inline=True)
    def math_atom(self, math_at):
        return str(math_at)

    @v_args(inline=True)
    def negative_number(self, num):
        return '-' + str(num)

    @v_args(inline=True)
    def atom(self, at):
        return str(at)

    @v_args(inline=True)
    def func(self, name, parameters):
        return name + '(' + parameters + ')'

    def func_name(self, items):
        return '.'.join(items)

    def parameters(self, items):
        return ', '.join(items)

    def args(self, items):
        return ', '.join(items)

    @v_args(inline=True)
    def normal_arg(self, name):
        return str(name)

    @v_args(inline=True)
    def args_unpacking(self, expr):
        # return '*(' + expr + ')'
        return '*' + expr

    def kwargs(self, items):
        return ', '.join(items)

    @v_args(inline=True)
    def normal_kwarg(self, name, value):
        return name + '=' + value

    @v_args(inline=True)
    def kwargs_unpacking(self, expr):
        # return '**(' + expr + ')'
        return '**' + expr

    @v_args(inline=True)
    def string_atom(self, s):
        return str(s)

    @v_args(inline=True)
    def string_op(self, s):
        return str(s)

    @v_args(inline=True)
    def concatenation(self, left, right):
        return left + ' + ' + right

    @v_args(inline=True)
    def logical_op(self, op):
        return str(op)

    @v_args(inline=True)
    def disjunction(self, left, right):
        return left + ' or ' + right

    @v_args(inline=True)
    def and_op(self, op):
        return str(op)

    @v_args(inline=True)
    def conjunction(self, left, right):
        return left + ' and ' + right

    @v_args(inline=True)
    def logical_atom(self, at):
        return str(at)

    @v_args(inline=True)
    def negation(self, at):
        return 'not ' + str(at)

    @v_args(inline=True)
    def comparison_atom(self, at):
        return str(at)

    @v_args(inline=True)
    def comparison_op(self, op):
        return str(op)

    @v_args(inline=True)
    def comparison(self, left, op, right):
        return left + ' ' + str(op) + ' ' + right
