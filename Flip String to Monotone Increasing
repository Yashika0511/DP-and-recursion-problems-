"""A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing."""
def minFlipsMonoIncr(S):
    dp = [0] * 2

    for i, c in enumerate(S):
        dp[0], dp[1] = dp[0] + (c == '1'), min(dp[0], dp[1]) + (c == '0')

    return min(dp[0], dp[1])
