# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            d[x] = d.setdefault(x, 0) + 1
            if d[x] > 1:
                return True
        
        return False

sol = Solution().containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])
print(sol)