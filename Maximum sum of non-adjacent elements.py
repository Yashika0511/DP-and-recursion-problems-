"""Given an array of ‘N’  positive integers, we need to return the maximum sum of the subsequence such that no two elements of
the subsequence are adjacent elements in the array."""

def maxSum(arr):
    n=len(arr)
    dp = [-1 for _ in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        k = arr[i]
        if i > 1:
            k += dp[i-2]
        notk = 0 + dp[i-1]
        dp[i] = max(k, notk)
    return dp[n-1]

# Iterative with O(1)m complexity
def maxSum2(arr):
    n=len(arr)
    prev = arr[0]
    prev2 = 0
    
    for i in range(1, n):
        k = arr[i]
        if i > 1:
            k += prev2
        notk = 0 + prev
        
        cur = max(k, notk)
        prev2 = prev
        prev = cur
        
    return prev
