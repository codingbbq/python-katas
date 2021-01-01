# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m  = {} # Use a hashmap / dictionary to store the list item and its indice
        for i in range(len(nums)):
            if nums[i] in m and i - m[nums[i]] <= k:
                return True
            else:
                m[nums[i]] = i

        return False

sol = Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
print(sol)
