"""You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations."""

def minimizeArrayValue(nums):
        maxim = nums[0]
        prefix_sum = nums[0]

        for idx in range(1, len(nums)):
            curr = nums[idx]
            prefix_sum += curr
            if curr > maxim:
                maxim = max(maxim, math.ceil(prefix_sum / (idx + 1)))


        return maxim
