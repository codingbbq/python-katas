# Happy number
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution:
    def isHappy(self, n: int) -> bool:
    
        while n <= 2147483647:
            sum = 0
            while n != 0:
                sum+= pow(n%10, 2)
                n = n//10

            print(sum)
            n = sum
            if n == 1:
                return True

        return False
        


sol = Solution().isHappy(n = 7)
print(sol)