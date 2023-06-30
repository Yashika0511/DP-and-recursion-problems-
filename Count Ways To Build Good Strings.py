"""Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at
each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be
large, return it modulo 109 + 7."""

def countGoodStrings(low, high, zero, one):
        dp = [1] + [0] * (high)
        mod = 10 ** 9 + 7
        for end in range(1, high+1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod

        return sum(dp[low : high+1]) % mod
