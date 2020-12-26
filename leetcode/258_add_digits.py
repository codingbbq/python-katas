# 258. Add Digits
# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = (num%10 + num//10)
        
        return num


sol = Solution().addDigits(num=100)
print(sol)