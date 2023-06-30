"""Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair.
At a time the frog can climb either one or two steps. A height[N] array is also given.
Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]),
where abs() means the absolute difference. 
We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1."""

def frogJump(height):
    n = len(height)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for i in range(1,n):
        j2= float('inf')
        j1= dp[i-1] + abs(height(i) - height(i-1))
        if i>1:
            j2= dp[i-2] + abs(height(i)- height(i-2))
        dp[i]=min(j1,j2) 
    return dp[n-1]    
