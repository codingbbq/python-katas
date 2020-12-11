
# 1450. Number of Students Doing Homework at a Given Time
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for x,y in zip(startTime, endTime):
            if x <= queryTime and y >= queryTime:
                ans+=1

        return ans

Solution().busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)
Solution().busyStudent(startTime = [4], endTime = [4], queryTime = 4)
Solution().busyStudent(startTime = [4], endTime = [4], queryTime = 5)

Solution().busyStudent(startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7)
Solution().busyStudent(startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5)

Solution().busyStudent(startTime = [16], endTime = [60], queryTime = 58)