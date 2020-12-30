# 1370. Increasing Decreasing String
# https://leetcode.com/problems/increasing-decreasing-string/

from typing import List

class Solution:
    def sortString(self, s: str) -> str:
        # Get the frequency of each characters and store it in a dictionary
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.setdefault(s[i], 0) + 1

        count = len(s)
        new_str = []

        # Run the loop until all the characters in the string are parsed
        while count > 0:

            # Use the character code from a to z i.e 97 to 122
            for i in range(97, 123):
                chri = chr(i)
                # Check if the character is present in freq and its count is > 0
                if chri in freq and freq[chri] > 0:
                    new_str.append(chri)
                    freq[chri]-=1
                    count-=1

            # Reverse so that we can execute step 4 and 5 i.e pick largets character
            for j in range(122, 96, -1):
                chrj = chr(j)
                if chrj in freq and freq[chrj] > 0:
                    new_str.append(chrj)
                    freq[chrj]-=1
                    count-=1

        return ''.join(new_str)

sol = Solution().sortString(s = "aaaabbbbcccc")
print(sol)