# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/
import sys
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        MIN_INT = -sys.maxsize - 1
        first, second, third = MIN_INT, MIN_INT, MIN_INT
        for x in nums:
            if x > first:
                first, second, third = x, first, second
            elif x != first and x > second:
                second, third = x, second
            elif x != first and x != second and x > third:
                third = x

        if third > MIN_INT:
            return third
        else:
            return first  

solution = Solution().thirdMax(nums = [5,2,4,1,3,6,0])
print(solution)