# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        for i, x in enumerate(A):
            # In Place Reverse of the List
            left, right = 0, len(x) - 1
            while left <= right:
                x[left], x[right] = x[right], x[left]
                # # Inverse
                # if x[left] == 1:
                #     x[left] = 0 
                # else:
                #     x[left] = 1

                # # If the left and right index are same, we have already taken care of the inverse in the above condition
                # if(left != right):
                #     if x[right] == 1:
                #         x[right] = 0
                #     else:
                #         x[right] = 1

                # Using BITWISE XOR
                x[left], x[right] = x[left] ^ 1, x[right] ^ 1
                left, right = left+1, right-1


            # Replace the list at the same position with the new list
            A[i] = x

        print(A)

Solution().flipAndInvertImage(A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])