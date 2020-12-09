# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        
        # Find the modulas of the number
        def modular(number):
            if number < 0:
                return number % -10
            else:
                return number % 10

        # Divide the number
        def divide(number):
            return int(number*1.0 / 10)

        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = - 2 ** 31 # -2147483648

        res = 0
        while x:
            pop = modular(x)
            x = divide(x)
            if res > divide(MAX_INT) or (res == divide(MAX_INT) and pop > 7):
                return 0
            if res < divide(MIN_INT) or (res == divide(MIN_INT) and pop < -8):
                return 0
            res = res * 10 + pop
        
        return res

Solution().reverse(x = -1234)