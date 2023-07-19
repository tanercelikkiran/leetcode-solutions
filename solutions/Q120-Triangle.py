from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        if n == 1:
            return triangle[0][0]
            
        for i in range(1, len(triangle)):
            for j in range(i+1):
                left = right = 10001

                if j-1 != -1:
                    left = triangle[i][j] + triangle[i-1][j-1]
                if j != i:
                    right = triangle[i][j] + triangle[i-1][j]

                triangle[i][j] = min(left, right)

        return min(triangle[-1])