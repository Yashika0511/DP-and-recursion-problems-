"""Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair.
#At a time we can climb either one or two steps.
#We need to return the total number of distinct ways to reach from 0th to Nth stair.
"""

def climbingStairs(n):
    f = [0, 1, 2]
    for i in range(3, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
