
# 运行python -m doctest -v lecture04.py进行样例测试
from math import pi,sqrt
def area(r, shape_constant):
    assert r>0,'A length must be positive'
    return r*r*shape_constant
def area_square(r):
    return area(r,1)
def area_circle(r):
    return area(r,pi)
def area_hexagon(r):
    return area(r,3*sqrt(3)/2)
area_square(3)



def sum_naturals(n):
    """Sum the first natural numbers
    >>> sum_naturals(5)
    15
    """
    total,k = 0,1
    while k<=n:
        total,k = total+k,k+1
    return total
def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    total,k = 0,1
    while k<=n:
        total,k=total+pow(k,3),k+1
    return total
"""Generalization"""
def identity(k):
    return k
def cube(k):
    return pow(k,3)
def summation(n,term):
    """test
    >>> summation(5,cube)
    225
    """
    total,k = 0,1
    while k<=n:
        total,k = total + term(k),k+1
    return total
# <consequent> if <predicate> else <alternative>
## if predicate is true,the value of the whole expression is the value of the <consequent>.otherwise,the value of the whole expression is the value of <alternative>
x = 0
print(abs(1/x if x!=0 else 0))