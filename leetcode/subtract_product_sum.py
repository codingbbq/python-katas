# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sum = 1, 0
        for x in str(n):
            prod = prod*int(x)
            sum+=int(x)

        return prod-sum

Solution().subtractProductAndSum(n = 234)

# The above solution uses type conversion from int to str and int wherever required
# either to go through the digits in loop or to multiply, add the number. 