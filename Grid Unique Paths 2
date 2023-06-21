"""We are given an “N*M” Maze. The maze contains some obstacles. A cell is ‘blockage’ in the maze if its value is -1. 
0 represents non-blockage. There is no path possible through a blocked cell.

We need to count the total number of unique paths from the top-left corner of the maze to the bottom-right corner. 
At every cell, we can move either down or towards the right."""


def countWays2(m, n, grid):
    dp = [[-1 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0 and grid[i][j] == -1:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            u,l=0,0
            if i > 0:
                u = dp[i-1][j]
            if j > 0:
                l = dp[i][j-1]
            dp[i][j] = u + l
    return dp[n-1][m-1]
