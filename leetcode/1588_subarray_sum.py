# 1588. Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = 0
        j = len(arr)
        ans = 0

        for x in range(len(arr)):
            for i in range(x, len(arr)):
                if len(arr[x:i+1])%2 != 0:
                    ans+= sum(arr[x:i+1])

        return ans


Solution().sumOddLengthSubarrays(arr = [1,4,2,5,3])