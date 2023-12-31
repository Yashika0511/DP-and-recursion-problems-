"""Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order."""

def permute(nums):
        res = []

        def backtrack(pointer):
            if pointer == len(nums):
                res.append(nums.copy())

            for i in range(pointer, len(nums)):
                nums[pointer], nums[i] = nums[i], nums[pointer]
                backtrack(pointer + 1)
                nums[pointer], nums[i] = nums[i], nums[pointer]
        backtrack(0)
        
        return res
