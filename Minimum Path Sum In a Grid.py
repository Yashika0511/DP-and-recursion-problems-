"""We are given an “N*M” matrix of integers. We need to find a path from the top-left corner to the bottom-right corner 
of the matrix, such that there is a minimum cost past that we select.

At every cell, we can move in only two directions: right and bottom. The cost of a path is given as the sum of values
of cells of the given matrix."""

def minPathSum(grid):
    n=len(grid)
    m=len(grid[0])
    for i in range(n):
        for j in range(m):
            if i==0:
                if j!=0:
                    grid[i][j]+=grid[i][j-1]
            elif j==0:
                if i!=0:
                    grid[i][j]+=grid[i-1][j]
            else:
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
    return grid[n-1][m-1]
