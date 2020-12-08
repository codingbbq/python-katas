# 1342. Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
                count+=1
            else:
                num-=1
                count+=1

        return count
       

Solution().numberOfSteps(num = 14)


'''
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        return self.numSteps(count, num)


    def numSteps(self, count: int, num: int) -> int:
        if(num == 0):
            return count

        if(num % 2 == 0):
            num //= 2
            count+=1
            return self.numSteps(count, num)
        else:
            num-= 1
            count+=1
            return self.numSteps(count, num)
    
    '''