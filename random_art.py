import random
from math import cos, sin, tan

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    rtrix = lambda x,y: random.triangular(0,x,y)
    rtriy = lambda x,y: random.triangular(0,y,x)
    rgau = lambda x,y: random.gauss(x,y)
    cos = lambda x:  math.cos(x)
    sin = lambda x: math.sin(x)

    def tritry():
        expr1 = lambda x, y: (x + y)/2
        expr2 = lambda x, y: (x - y)/2
        expr3 = lambda x, y: x * y
        return random.choice([expr1, expr2, expr3])
    exprs_1 = ['cos(z)', 'sin(z)', 'tan(z)']
    exprs_2 = ['random.triangular(x,y)',
               'random.gauss(x,y)',
               ]
    big_expr = random.choice(exprs_1)

    for expr in exprs_1:
        big_expr = big_expr.replace('z', expr)
    big_expr = big_expr.replace('z', random.choice(exprs_2))
    return big_expr

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)
