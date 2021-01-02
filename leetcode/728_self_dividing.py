# 728. Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # To Store the output
        ans = []
        for x in range(left, right+1):
            # if it is 1 digit number append it to the ans array
            if x%10 == x:
                ans.append(x)
                continue
            
            # Check if each digit in the number is divisible by the number
            isTrue = self.checkNos(x)
            if isTrue:
                ans.append(x)
            
        return ans


    def checkNos(self, num):
        # A variable that stores increments if all the digits are divisible by number
        count = 0
        y = num
        # Loop through each digit
        while num > 0:
            val=num%10
            # Check for divisiblity by zero
            if val>0 and y%val == 0:
                count+=1
            else:
                # Return false if even one digit is not divisible
                return False
            num//=10

        # If count and len of string are equal, all the digits were divisible by number      
        if len(str(y)) == count:
            return True

sol = Solution().selfDividingNumbers(left = 1, right = 22)
print(sol)