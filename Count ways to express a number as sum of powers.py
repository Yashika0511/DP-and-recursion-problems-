"""Given two integers x and n, we need to find number of ways to express x as sum of n-th powers of unique natural numbers.
It is given that 1 <= n <= 20."""

def countWaysHelper(x,n,num):
 
    val = (x - pow(num, n))
    if (val == 0):
        return 1
    if (val < 0):
        return 0
    return countWaysHelper(val, n, num + 1) + countWaysHelper(x, n, num + 1)

def countWays(x,n):
    return countWaysHelper(x, n, 1)
