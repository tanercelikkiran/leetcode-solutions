class Solution:
    def reverse(self, x: int) -> int:
        ans = 0 # 32-bit signed integer
        isNegative = False # is x negative?
        if x < 0: # if x is negative
            isNegative = True # set isNegative to True
            x = -x # make x positive
        while x: # x not equal to 0
            ans = ans * 10 + x % 10 # add the last digit of x to ans and move ans to the left
            x //= 10 # move x to the right
        if isNegative: # if x was negative
            ans = -ans # make ans negative
        return ans if -2**31 <= ans <= 2**31 - 1 else 0 # return ans if it is in the range of 32-bit signed integer