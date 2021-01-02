# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove the spaces before and after of the word
        # Split the string on spaces. It returns a list
        # Take the last item of the list and then use the len method to return the length
        return len(s.strip().split(" ")[-1])

sol = Solution().lengthOfLastWord(s = "a ")
print(sol)