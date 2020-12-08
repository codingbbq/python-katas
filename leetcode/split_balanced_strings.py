# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # python dict to keep track of R and L
        obj = { 'R':0, 'L':0 }
        # Keep track of the balanced strings
        total = 0

        for i, x in enumerate(s):

            # Check for 'R and increment the R count
            if(s[i] == 'R'):
                obj['R']+=1

            # Check for 'L' and increment the L count
            if(s[i] == 'L'):
                obj['L']+=1

            # When to split the string? Check for R and L count if they are equal.
            if(obj['R'] == obj['L']):
                # Increment the total
                total+=1
                # Reset R and L count
                obj['R'] = 0
                obj['L'] = 0


        return total

Solution().balancedStringSplit(s = "RLLLLRRRLR")

# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.