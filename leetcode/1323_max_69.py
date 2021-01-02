# 1323. Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the num into array/list
        max = str(num)
        arr = [x for x in str(num)]
        for y in range(len(arr)):
            # Replace the first occurance of 6 to 9,
            # it will result in max number
            if arr[y] == '6':
                arr[y] = '9'
                max = int(''.join(arr))
                break

        return max


sol = Solution().maximum69Number(num = 9669)
print(sol)