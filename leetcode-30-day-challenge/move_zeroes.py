# Move Zeroes
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Solution using in place List shift
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        
        return nums

sol = Solution().moveZeroes(nums = [0,1,0,3,12])
print(sol)