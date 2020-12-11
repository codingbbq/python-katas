# 169. Majority Element
# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key, val = 0, 0
        majority = {}
        for x in nums:
            majority[x] = majority.setdefault(x, 0) + 1
            if majority[x] > val:
                val = majority[x]
                key = x

        return key
Solution().majorityElement(nums = [2,2,1,1,1,2,2])