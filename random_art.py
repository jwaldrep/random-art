import random
from math import cos, sin, tan, log10

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

def avg(x, y): return (x + y) / 2;

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""


    exprs_1 = ['cos(z)', 'sin(z)', 'tan(z)',
               'z**2',
               ]
    exprs_2 = [#'random.triangular(x,y)',
               #'random.gauss(x,y)',
               'avg(x,y)',
               '(x*y)',
               'x', 'y',
            #    'random.expovariate(x/(y+1))',
               ]

    big_expr = random.choice(exprs_1)

    for _ in range(random.randrange(30)):
        big_expr = big_expr.replace('z', random.choice(exprs_1))

    big_expr = big_expr.replace('z', random.choice(exprs_2))

    return big_expr

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)
