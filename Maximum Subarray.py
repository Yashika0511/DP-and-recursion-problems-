"""Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum."""

def maxSubArray(nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
