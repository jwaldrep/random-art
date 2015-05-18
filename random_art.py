import random
from math import cos, sin, tan, log10, sqrt

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

def avg(x, y): return (x + y) / 2;
def circle(x,y):
    radius = random.random()
    thickness = random.random()/4
    return 1 if abs(sqrt(x**2 + y**2) - radius) < thickness else 0
def grad(x,y): return sqrt( (x)**2 + (y)**2 );
def div(x,y):
    if y != 0:
        return x / y
    if x != 0:
        return y / x
    return x
def to_the(x,y):
    if x == 0:
        return x
    return abs(x)**y

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""


    exprs_1 = ['cos(z)', 'sin(z)', 'tan(z)',
               #'z**2',
            #    'sqrt((z+.1)/1.1)'
               ]
    exprs_2 = [
            #    'random.triangular(x,y)',
            #    'random.gauss(x,y)',
#               'avg(x,y)',
            #    '(x*y)',
                'to_the(x,y)',
            #     'x', 'y',
            #    'circle(x,y)',
            #    'grad(x,y)',
            #    'div(x,y)'
                # 'random.expovariate(x/(y+1))',
               ]

    big_expr = random.choice(exprs_1)

    for _ in range(random.randrange(30)):
        big_expr = big_expr.replace('z', random.choice(exprs_1))

    big_expr = big_expr.replace('z', random.choice(exprs_2))

    for _ in range(random.randrange(2)): #this may make the computer explode
        big_expr = big_expr.replace('x', random.choice(exprs_2))
        big_expr = big_expr.replace('y', random.choice(exprs_2))
        big_expr = big_expr.replace('z', random.choice(exprs_2))



    return big_expr

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)
