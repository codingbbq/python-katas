# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x*x for x in nums])


Solution().sortedSquares(nums = [-4,-1,0,3,10])