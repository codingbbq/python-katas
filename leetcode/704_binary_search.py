# 704. Binary Search
# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left  = 0
        right = len(nums) - 1
        index = (left + right)//2
        while left <= right:
            if nums[index] == target:
                return index
            else:
                if nums[index] > target:
                    right  = index - 1
                    index = (left + right)//2
                else:
                    left = index+1
                    index = (left+right)//2

        return -1


sol = Solution().search(nums = [-1,0,3,5,9,12], target = 12)
print(sol)