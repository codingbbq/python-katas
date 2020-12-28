# 1287. Element Appearing More Than 25% In Sorted Array
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        # Find the length of the array
        size = len(arr)
        #count = 25% of size
        count = 0.25*size
        # Use dictionary to store the count
        d = {}
        for i in range(size):
            d[arr[i]] = d.setdefault(arr[i], 0) + 1
            if d[arr[i]] > count:
                return arr[i]

sol = Solution().findSpecialInteger(arr = [1,2,3,3])
print(sol)