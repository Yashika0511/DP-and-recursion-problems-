"""A thief needs to rob money in a street. The houses in the street are arranged in a circular manner.
Therefore the first and the last house are adjacent to each other. 
The security system in the street is such that if adjacent houses are robbed, the police will get notified.

Given an array of integers “Arr” which represents money at each house,
we need to return the maximum amount of money that the thief can rob without alerting the police.
"""

def rob(arr):
        if len(nums) <= 2:
            return max(arr)

        def helper(arr):
            prev, cur = 0, 0
            for n in arr:
                prev, cur = cur, max(n + prev, cur)
            return cur

        return max(helper(arr[1:]), helper(arr[:-1]))
