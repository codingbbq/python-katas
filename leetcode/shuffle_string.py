# 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create a dictionary to store indices as key and s[indices] as value
        o = {}
        # crate a list where shuffled values will be stored
        shuffle = []
        # enumerate over the indices
        for i,x in enumerate(indices):
            o[x] = s[i]

        for x in range(len(s)):
            shuffle.append(o[x])

        return ''.join(shuffle)

Solution().restoreString(s = "aiohn", indices = [3,1,4,2,0])
# Output = nihao