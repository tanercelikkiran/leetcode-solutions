class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        while True:
            for j in range(left, right+1):
                res.append(matrix[up][j])
            up += 1
            if up > down:
                break
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for j in range(right, left-1, -1):
                res.append(matrix[down][j])
            down -= 1
            if up > down:
                break
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res