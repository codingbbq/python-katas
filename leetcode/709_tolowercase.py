# 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str: str) -> str:
        newStr = []
        for s in str:
            if(ord(s) >= 65 and ord(s) <=90):
                newStr.append(chr(ord(s) + 32))
            else:
                newStr.append(s)
        
        return ''.join(newStr)

Solution().toLowerCase(str = "Hello")