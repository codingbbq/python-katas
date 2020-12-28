# 1252. Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        odd = 0

        # Initialize the matrix with all the 0
        mat = [[0 for c in range(m)] for r in range(n)]

        # Loop through the matrix based on the index and increment
        for i in indices:
            for x in range(m):
                mat[i[0]][x]+=1

            for y in range(n):
                mat[y][i[1]]+=1

        # Loop again through the matrix to find the odd number
        for a in range(len(mat)):
            for b in range(len(mat[a])):
                if mat[a][b]%2 != 0:
                    odd+=1

        return odd
sol = Solution().oddCells(n = 2, m = 3, indices = [[0,1],[1,1]])
print(sol)