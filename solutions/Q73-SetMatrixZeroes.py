from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        changes = []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    changes.append((i, j))

        for i, j in changes:
            for k in range(n):
                matrix[k][j] = 0
            for k in range(m):
                matrix[i][k] = 0