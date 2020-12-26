# 1441. Build an Array With Stack Operations
# https://leetcode.com/problems/build-an-array-with-stack-operations/

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        new_array = []
        index = 0
        for i in range(1,n+1):
            new_array.append("Push")
            if target[index] == i:
                index+=1
            else:
                new_array.append("Pop")

            if index == len(target):
                break

        return new_array

sol = Solution().buildArray(target = [1,2], n = 4)
print(sol)