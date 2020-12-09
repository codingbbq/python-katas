# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if self.countDigit(x) % 2 == 0:
                count+=1

        print(count)

    # Find the count of digits in each number
    def countDigit(self, x:int) -> int:
        digit = 0
        while x!=0:
            x//=10
            digit+=1

        return digit


Solution().findNumbers(nums = [555,901,482,1771])