# 1534. Count Good Triplets
# https://leetcode.com/problems/count-good-triplets/

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                         if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count+=1

        return count


# Solution().countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3)

Solution().countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1)