import math

def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def sub(t1, t2):
    return t1[0] - t2[0], t1[1] - t2[1]


def mult(a, x):
    return a*x[0], a*x[1]

def div(x, a):
    return x[0]/a, x[1]/a

def dot(t1, t2):
    return t1[0]*t2[0] + t1[1]*t2[1]

def norm(x):
    return math.sqrt(dot(x, x))

def unit(x):
    if norm(x):
        return div(x, norm(x))
    
    return 0, 1

def closest(x):
    return int(round(x[0])), int(round(x[1]))
