# 905. Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/

from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i]%2 > A[j]%2:
                A[i],A[j] = A[j],A[i]

            if A[i]%2==0: i+=1
            if A[j]%2==1: j-=1

        print(A)

Solution().sortArrayByParity(A = [1,0,3])