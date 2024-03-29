"""Q1: Count Stair Ways"""
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n<=1:
        return 1
    else: 
      return count_stair_ways(n-1) + count_stair_ways(n-2)
"""Q2: Count K"""
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        total = 0
        i=1
        while i<=k:
            total+=count_k(n-i,k)
            i+=1
        return total

        
