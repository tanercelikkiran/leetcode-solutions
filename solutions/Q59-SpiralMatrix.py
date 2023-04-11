from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1
        x = 0
        y = 0

        min_x, min_y = 0, 0

        max_x, max_y = n-1, n-1

        ans = [[0]*n for i in range(n)]

        while count < n**2+1:
            for _ in range(min_x, max_x+1):
                ans[y][x] = count
                count += 1
                x += 1
            min_y += 1
            x, y = max_x, min_y

            for _ in range(min_y, max_y+1):
                ans[y][x] = count
                count += 1
                y += 1
            max_x -= 1
            x, y = max_x, max_y

            for _ in range(min_x, max_x+1):
                ans[y][x] = count
                count += 1
                x -= 1
            max_y -= 1
            x, y = min_x, max_y

            for _ in range(min_y, max_y+1):
                ans[y][x] = count
                count += 1
                y -= 1
            min_x += 1
            x, y = min_x, min_y

        return ans