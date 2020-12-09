# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        print(self.findIndex(target, low, high, nums))

    def findIndex(self, target:int, low:int, high:int, nums: List[int]) -> int:
        if high >= low:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.findIndex(target, low, mid-1, nums)
            else:
                return self.findIndex(target, mid+1, high, nums)
        
        else:
            return high+1



Solution().searchInsert(nums = [1,3,5,7,9], target = 7)