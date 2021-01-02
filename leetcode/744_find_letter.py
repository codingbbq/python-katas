# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # Check for target z. Then the next greatest letter will begin from "a"
        # So we are setting t = 96 one less than that of value of "a"
        t = ord(target)
        if t == 122:
            t = 96

        # The letters list is sorted, so we can directly return the next greatest value once we find it.
        for i in range(len(letters)):
            if ord(letters[i]) > t:
                return letters[i]

        # If we have not found it, the first element can be considered as the greatest value.
        return letters[0]

sol = Solution().nextGreatestLetter(letters = ["c", "f", "j"],target = "j")
print(sol)