"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array."""

def subarraySum(nums, k):
        dp = {0:1}
        sums = 0
        count = 0
        for num in nums:
            sums += num
            diff = sums - k
            if diff in dp:
                count += dp[diff]
            dp[sums]= dp.get(sums,0)+1
        return count
