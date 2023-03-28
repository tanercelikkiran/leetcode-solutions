class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: # if n is 0
            return 1 # return 1
        else: # if n is not 0
            for i in range(abs(n)-1): # iterate through n
                x *= x # multiply x by itself
            if n < 0: # if n is negative
                x = 1/x # divide 1 by x
            return x # return x