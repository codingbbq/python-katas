# 1525. Number of Good Ways to Split a String
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/


from typing import List

class Solution:
    def numSplits(self, s: str) -> int:
        count: int = 0
        left = {}
        right = {}
        for x in s:
            right[x] = right.setdefault(x, 0) + 1
        
        for x in s:
            left[x] = left.setdefault(x, 0) + 1
            right[x] -= 1
            if right[x] == 0:
                del right[x]

            if len(right) == len(left):
                count+=1

        return count


Solution().numSplits(s = "aacaba")