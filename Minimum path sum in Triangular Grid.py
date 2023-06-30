"""We are given a Triangular matrix. We need to find the minimum path sum from the first row to the last row.

At every cell we can move in only two directions: either to the bottom cell (↓) or to the bottom-right cell(↘)"""

def triangleSum(triangle):
    dp = [[0 for j in range(n)] for i in range(n)]
    
    for j in range(n):
        dp[n-1][j] = triangle[n-1][j]
    
    for i in range(n-2, -1, -1):
        for j in range(i, -1, -1):
            dow = triangle[i][j] + dp[i+1][j]
            dia= triangle[i][j] + dp[i+1][j+1]
            
            dp[i][j] = min(dow, dia)
    
    return dp[0][0]
