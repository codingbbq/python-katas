# 67. Add Binary
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_l = max(len(a), len(b))
        strlen = max_l - 1
        a = a.zfill(max_l)
        b = b.zfill(max_l)
        c = ''
        carry = 0
        while strlen >= 0:
            if a[strlen] == '1' and b[strlen] == '1':
                if carry == 1:
                    c = '1' + c
                    carry = 1
                else:
                    c = '0' + c
                    carry = 1
            elif a[strlen] == '0' and b[strlen] == '0':
                if carry == 1:
                    c = '1' + c
                    carry = 0
                else:
                    c = '0' + c
                    carry = 0
            elif (a[strlen] == '1' and b[strlen] == '0') or (a[strlen] == '0' and b[strlen] == '1'):
                if carry == 1:
                    c = '0' + c
                    carry = 1
                else:
                    c = '1' + c
                    carry = 0
            
            strlen-=1

        if carry == 1:
            c = '1' + c

        
        return c

solution = Solution().addBinary(a = "1010", b = "1011")
print(solution)