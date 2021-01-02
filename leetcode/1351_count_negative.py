# 1351. Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for xi in range(len(grid)):
            for yi in range(len(grid[xi])):
                if grid[xi][yi] < 0:
                    count+=1

        return count
        


sol = Solution().countNegatives(grid = [[-1]])
print(sol)