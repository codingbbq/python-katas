# 1464. Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort the array and then use the highest two numbers to return the calculation
        nums = sorted(nums, reverse=True)
        return (nums[0] - 1)*(nums[1]-1)

sol = Solution().maxProduct(nums = [3,7])
print(sol)