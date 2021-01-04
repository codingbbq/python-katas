# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        end = len(s)
        
        for i in range(1, end//2 + 1):
            # If the first ith characters is equal to the last ith characters
            firstIth = s[:i]
            lastIth = s[-i:]
            size = len(firstIth)
            repeat = end//size
            if firstIth == lastIth:
                if s == firstIth * repeat:
                    return True


        return False

sol = Solution().repeatedSubstringPattern(s = "babbabbabbabbab")
print(sol)