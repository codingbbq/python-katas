# 541. Reverse String II
# https://leetcode.com/problems/reverse-string-ii/

class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)


sol = Solution().reverseStr(s = "abcdefg", k = 8)
print(sol)