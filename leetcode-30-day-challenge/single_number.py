# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash map
        traversed = {}
        for x in nums:
            traversed[x] = traversed.setdefault(x, 0) + 1
        
        for i in traversed:
            if traversed[i] == 1:
                return i


sol = Solution().singleNumber(nums = [4,1,2,1,2])
print(sol)