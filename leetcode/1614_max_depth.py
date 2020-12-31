# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

from typing import List

class Solution:
    def maxDepth(self, s: str) -> int:
        # Loop through each of the string
        # Keep a count of open brackets
        # Keep a count of max
        open = 0
        max = 0
        for x in s:
            if x == "(":
                open+=1
                if open > max:
                    max = open

            if x == ")":
                open-=1

        # Since it is guaranteed that we hav a VPS, we can directly return max
        return max

sol = Solution().maxDepth(s = "(1+(2*3)+((8)/4))+1")
print(sol)