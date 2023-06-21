"""Given two values M and N, which represent a matrix[M][N]. We need to find the total unique paths from the top-left cell 
(matrix[0][0]) to the rightmost cell (matrix[M-1][N-1]).

At any cell we are allowed to move in only two directions:- bottom and right.
"""
def countWays(m,n):
    dp = [[-1 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j]=1
                continue
            u,l=0,0
            if i > 0:
                u = dp[i-1][j]
            if j > 0:
                l = dp[i][j-1]
            dp[i][j] = u + l
    return dp[m-1][n-1] 
