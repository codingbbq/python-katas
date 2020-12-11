# 1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        j = len(mat) - 1
        sum = 0
        while i<=j:
            if i==j:
                sum+= mat[i][len(mat[i])//2]
            else:
                sum+= mat[i][i] + mat[i][(len(mat[i]) - 1) - i] + mat[j][i] + mat[j][(len(mat[j]) - 1) - i]
            i+=1
            j-=1
        return sum
Solution().diagonalSum(mat = [[5]])