class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0  # left is the smallest integer that is greater than the square root of x
        right = x+1 # right is the smallest integer that is greater than x
        while left < right: # binary search
            mid = left + (right-left) // 2 # m is the middle integer
            if mid * mid > x: # if m is greater than the square root of x
                right = mid # set right to m
            else: # if m is less than or equal to the square root of x
                left = mid + 1 # set left to m+1
        return left-1 # return the largest integer that is less than or equal to the square root of x