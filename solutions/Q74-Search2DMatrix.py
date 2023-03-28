from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # binary search on row
        left = 0 # first row
        right = len(matrix)-1 # last row 
        rowMid = 0 # middle for row
        colMid = 0 # middle for column

        while left <= right: # binary search on row
            rowMid = (left + right) // 2 # middle for row
            if matrix[rowMid][0] == target: # if target is in the first column
                return True # return true
            elif matrix[rowMid][0] > target: # if target is less than the first column
                right = rowMid - 1 # move right to the left
            else: # if target is greater than the first column
                left = rowMid + 1 # move left to the right

        if matrix[rowMid][0] > target: # if target is less than the first column
            rowMid -= 1 # move rowMid to the left

        left = 0 # first column
        right = len(matrix[0])-1 # last column

        while left <= right: # binary search on column
            colMid = (left + right) // 2 # middle for column
            if matrix[rowMid][colMid] == target: # if target is in the middle
                return True # return true
            elif matrix[rowMid][colMid] > target: # if target is less than the middle
                right = colMid - 1 # move right to the left
            else: # if target is greater than the middle
                left = colMid + 1 # move left to the right
        return False # if target is not found, return false