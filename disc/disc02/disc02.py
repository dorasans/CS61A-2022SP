## finish question4
"""
Q5:Make Keeper
"""
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    def even(f):
        i=1
        while i<=n:
            if f(i):
                print(i)
            i+=1
    return even

    """
    Q6: Curry2 Diagram
    """
"""
Q7: HOF Diagram Practice
"""
n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y:y())(f) #先调用f然后返回的h赋值给y,y()运行后返回x+1
print(g)

"""
Q8: Match Maker
"""
def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    """
    方法一
    """
    # def check(n):
    #     i=0
    #     while 10**(i+k)<n:
    #         if (n//(10**i))%10!=(n//(10**(i+k))%10):
    #             return False
    #         i+=1
    #     return True
    # return check
    """
    方法二
    """
    def check(x):
        while x//(10**k):
            if x%10!=x//(10**k)%10:
                return False
            x//=10
        return True
    return check