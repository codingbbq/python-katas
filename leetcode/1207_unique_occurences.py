# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        oc = {}
        for x in arr:
            if x in oc:
                oc[x] = oc[x]+1 
            else:
                oc[x] = 1

        # Check if there is unique
        return len(set(oc.values())) == len(oc.values())


Solution().uniqueOccurrences(arr = [1,2,2,1,1,3])
