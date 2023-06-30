"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of 
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of 
"abcde" while "aec" is not)."""

def isSubsequence(s, t):
        s, t = "!" + s, "!" + t
        m, n = len(s), len(t)
        dp = [[0] * m for _ in range(n)] 
        for i in range(n): dp[i][0] = 1
   
        for i,j in product(range(1, n), range(1, m)):
            if s[j] == t[i]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]
