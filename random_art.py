import random
from math import cos, sin, tan, log10, sqrt, pi
from math import exp as ep


def avg(x, y):
    return (x + y) / 2


def circle(x, y):
    radius = random.random()
    thickness = random.random()/4
    return 1 if abs(sqrt(x**2 + y**2) - radius) < thickness else 0

def grad(x,y):
    return sqrt( (x)**2 + (y)**2 )

def grad_offset(x, y):
    cx = random.random()
    cy = random.random()
    return sqrt((x - cx)**2 + (y - cy)**2)


def div(x, y):
    if y != 0:
        return x / y
    if x != 0:
        return y / x
    return x


def to_the(x, y):
    if x == 0:
        return x
    return abs(x)**y


def recip(x):
    if x == 0:
        return x
    return 1/x


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates.

    exprs_1 contains strings of function calls for single-parameter functions
            These must use z as a variable
    exprs_2 contains strings of function calls for 2-parameter (x,y) functions

    A nested string of single function calls (of random length)
            is built by recursively replacing z
    Then a second round of replacements adds a random number of
            2-parameter functions to the inside

    The string is returned, with the intention of being called via eval()
    """

    exprs_1 = ['cos(z)', 'sin(z)',
               'cos(z*3*pi)', 'sin(z*3*pi)',
               'z**2',
               # 'sqrt(abs(z))',
               # 'z/2',
               #'recip(z)',
               # 'ep(z)',
               ]

    exprs_2 = [# 'cos(pi*x*y)',
               # 'avg(x,y)',
               # '(x*y)',
               # 'to_the(x,y)',
               # 'x', 'y',
               # 'circle(x,y)',
               'grad(x,y)',
               'div(x,y)',
               'cos(5*pi*x)*sin(5*pi*y)',
               'cos(5*pi*x**2)*sin(5*pi*y**2)',
               # 'cos(y)*sin(x)'
               # 'random.triangular(x,y)',
               # 'random.gauss(x,y)',
               ]

    big_expr = random.choice(exprs_1)

    for _ in range(random.randrange(5)):
        big_expr = big_expr.replace('z', random.choice(exprs_1))

    big_expr = big_expr.replace('z', random.choice(exprs_2))

    for _ in range(random.randrange(3)):  # this may make the computer explode
        big_expr = big_expr.replace('x', random.choice(exprs_1))
        big_expr = big_expr.replace('y', random.choice(exprs_1))
        big_expr = big_expr.replace('z', random.choice(exprs_2))

    return big_expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)
