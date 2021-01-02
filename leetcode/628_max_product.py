# 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a, b = 1,1
        # Sort the array
        nums = sorted(nums, reverse=True)
        a*=nums[0]*nums[1]*nums[2] # Product of positive numbers
        b*=nums[0]*nums[-1]*nums[-2] # Product of highest two negative numbers and a positive number
        return max(a, b)

sol = Solution().maximumProduct(nums = [-1,-2,-3])
print(sol)