# 1374. Generate a String With Characters That Have Odd Counts
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:

    # If the n is even, then (1, n-1) can be the combination
    # If the n is odd, then directly print n times the letter
        if n%2 == 0:
            return chr(97) + chr(98) * (n-1)
        else:
            return str(chr(97)*n)


sol = Solution().generateTheString(n = 7)
print(sol)