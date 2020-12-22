# 1290. Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution:
    def getDecimalValue(self, head) -> int:
        s = ''.join(map(str, head))
        return int(s, 2)

solution = Solution().getDecimalValue(head=[0,1,0])
print(solution)