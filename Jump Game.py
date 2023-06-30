"""You are given an integer array nums. You are initially positioned at the array's first index, and each element 
in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise."""


def canJump(nums):
        n=len(nums)
        dp=[False for _ in range(n)]
        dp[0]=True

        for i in range(n):
            if dp[i]:   # if this position is reachable
                for j in range(1,nums[i]+1):
                    if i+j<n:
                        dp[i+j]=True
                    if i+j==n-1:
                        return True
        return dp[n-1]
