"""
Q1:
1.12
2.19
3.12
4. one and three have the same output,because they all get into the first if statements,and ignore the other if or elif statements,and return the same result.
"""
"""
Q2: Jacket Weather?
"""
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return temp<60 or raining
"""
Q3: If Function vs Statement
"""
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return False
def true_func():
    "*** YOUR CODE HERE ***"
    print("Welcome to")
def false_func():
    "*** YOUR CODE HERE ***"
    print("61A")

"""
Q4: Square So Slow
1.x/0 will never be executed,because it is an infinite loop,and so_slow(5) must be executed before square()
"""

"""
Q5: Is Prime?
"""
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    prime_num = 2
    while prime_num<n:
        if n%prime_num==0:
            return False
        prime_num+=1
    return True

"""
Q6: Fizzbuzz
"""
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    g=1
    while g<=n:
        if g%15==0:
            print("fizzbuzz")
        elif g%5==0:
            print("buzz")
        elif g%3==0:
            print("fizz")
        else:
            print(g)
        g+=1

"""
Q7: Assignment Diagram
x    x=3
y    y=3
x    x=9
"""

"""
Q8: def Diagram
double    func triple(x) [parent=Global]
triple    func triple(x) [parent=Global]
hat       func double(x) [parent=Global]
"""