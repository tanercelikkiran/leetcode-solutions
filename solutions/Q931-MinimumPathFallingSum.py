from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        dp = []
        dp.append(matrix[0])
        for i in range(0, n-1):
            arr = []
            for j in range(n):
                if j == 0:
                    arr.append(min(dp[i][j], dp[i][j+1])+matrix[i+1][j])
                elif j == n-1:
                    arr.append(min(dp[i][j], dp[i][j-1])+matrix[i+1][j])
                else:
                    arr.append(min(dp[i][j], dp[i][j+1], dp[i][j-1])+matrix[i+1][j])
            dp.append(arr)
            
        return min(dp[-1])