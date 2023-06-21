"""Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed)
parentheses substring.
"""

def longestValidParentheses(s):
        n = len(s)
        dp = [0] * n
        ans = 0
        
        for i in range(1,n):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i-2] + 2;
            elif s[i] == ')' and s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2;
            ans = max(ans, dp[i])
        
        return ans
