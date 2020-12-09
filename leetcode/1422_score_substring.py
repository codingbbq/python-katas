# 1422. Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/
# Count 0s in the left substring and 1s in the right substring

class Solution:

    def maxScore(self, s: str) -> int:
        # Convert the string to list
        slist = list(s)
        max = 0

        # Loop over the list from 0th index to n-1th index. 
        # We want both the left and right list not to be empty
        for i in range(len(slist) - 1):
            l, r = 0, 0
            # left of the substring
            left = slist[:i+1]
            l = left.count('0')
            # right of the substring
            right = slist[i+1:]
            r = right.count('1')
            # Store the count of Left + Right only if it is max than previous count
            if(l + r > max):
                max = l+r

        return max

Solution().maxScore(s = "00")