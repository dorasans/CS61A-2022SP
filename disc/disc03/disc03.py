"""
Q1: Warm Up: Recursive Multiplication
"""
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return m
    else: 
        return m+multiply(m,n-1)

"""
Q2: Recursion Environment Diagram
"""
"""
Q3: Find the Bug
"""
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n==1:
        return 1
    else:
        return n * skip_mul(n - 2)

"""
Q4: Recursive Hailstone
"""
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    # 我的解法
    # k=0
    # if n==1:
    #     print(1)
    #     return k+1
    # if n%2==0:
    #     print(n)
    #     k=hailstone(n//2)
    #     return k+1
    # else:
    #     print(n)
    #     k=hailstone(n*3+1)
    #     return k+1
    #官方解法
    print(n)
    if n==1:
        return 1
    elif n%2==0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(n*3+1)

"""
Q5: Merge Numbers
"""
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    # 需要注意的是此处的n1和n2上的digit都是按降序排列的
    "*** YOUR CODE HERE ***"
    if n1==0:
        return n2
    elif n2==0:
        return n1
    elif n1%10<n2%10:
        return merge(n1//10,n2)*10+n1%10
    else:
        return merge(n1,n2//10)*10+n2%10

"""
Q6: Is Prime
"""
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(k):
        if k==n:   #could be replace with k>n**0.5
            return True
        elif n%k==0:
            return False
        else:
            return helper(k+1)
    return helper(2)
