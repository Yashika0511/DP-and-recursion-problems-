"""A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice,
or Learning New Moves) each day. There are merit points associated with performing an activity each day. 
The same activity can’t be performed on two consecutive days. 
We need to find the maximum merit points the ninja can attain in N Days.

We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day. 
Our task is to calculate the maximum number of merit points that the ninja can earn"""

def ninjaTraining(n,points):
    dp = [[0 for j in range(4)] for i in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for i in range(1, n):
        for j in range(4):
            dp[i][j] = 0
            for k in range(3):
                if k != j:
                    temp = points[i][k] + dp[day - 1][k]
                    dp[i][j] = max(dp[i][j], temp)

    return dp[n - 1][3]
