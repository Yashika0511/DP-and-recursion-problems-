"""This is a follow-up question to “Frog Jump” discussed in the previous question. 
In the previous question, the frog was allowed to jump either one or two steps at a time. In this question, 
the frog is allowed to jump up to ‘K’ steps at a time. 
If K=4, the frog can jump 1,2,3, or 4 steps at every index."""

import sys
def frogJump2(height, k):
    n=len(height)
    dp = [-sys.maxsize] * n
    dp[0] = 0
    for i in range(1, n):
        st = sys.maxsize
        for j in range(1, k+1):
            if i-j >= 0:
                jump = dp[i-j] + abs(height[i] - height[i-j])
                st = min(jump, mmSteps)
        dp[i] = st
    return dp[n-1]
