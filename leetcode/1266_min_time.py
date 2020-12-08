# 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minTime = 0
        for i in range(len(points) - 1):
            x = abs(points[i][0] - points[i+1][0])
            y = abs(points[i][1] - points[i+1][1])
            minTime+= max(x,y)

        return minTime

Solution().minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]])