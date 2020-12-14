# 1684. Count the Number of Consistent Strings
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for x in words:
            if set(x).issubset(set(allowed)):
                count+=1

        return count


solution = Solution().countConsistentStrings("abc", words = ["a","b","c","ab","ac","bc","abc"])
print(solution)