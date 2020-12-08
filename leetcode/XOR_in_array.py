# 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            xor ^= start + 2*i

        return xor

Solution().xorOperation(n = 4, start = 3)