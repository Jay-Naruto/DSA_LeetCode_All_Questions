# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        maps = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in maps:
                return [i, maps[val]]
            maps[nums[i]] = i

# Runtime: 38 ms, faster than 78.08% of Python online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 25.70% of Python online submissions for Two Sum.