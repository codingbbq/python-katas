# Happy number
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n > 1:
            sum = 0
            while n != 0:
                sum+= pow(n%10, 2)
                n = n//10
                
            if sum in seen:
                return False
            else:
                seen[sum] = True
            n = sum

        return True
        


sol = Solution().isHappy(n = 2)
print(sol)