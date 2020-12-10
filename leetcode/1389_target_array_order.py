# 1389. Create Target Array in the Given Order
# https://leetcode.com/problems/create-target-array-in-the-given-order/

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for x,y in zip(nums,index):
            target.insert(y,x)

        return target


Solution().createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])