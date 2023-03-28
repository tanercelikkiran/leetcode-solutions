class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0 # index of s
        n = len(s) # length of s
        sign = 1 # sign of the number

        while i < n and s[i] == ' ': # skip all the spaces
            i += 1 # move i to the right

        if i >= n: # if i is out of range
            return 0 # return 0
        
        if s[i] == '-': # if s[i] is '-'
            sign = -1 # set sign to -1
            i += 1 # move i to the right
        elif s[i] == '+': # if s[i] is '+'
            i += 1 # move i to the right

        ans = 0 # answer
        while not (i >= len(s) or s[i] < '0' or s[i] > '9'): # while s[i] is a digit
            ans = ans*10 + int(s[i]) # add s[i] to ans and move ans to the left
            i += 1 # move i to the right
        ans *= sign # multiply ans by sign
        if ans >= 2**31: # if ans is greater than or equal to 2**31
            return 2**31 - 1 # return max value of 32-bit signed integer
        elif ans <= -2**31: # if ans is less than or equal to -2**31
            return -2**31  # return min value of 32-bit signed integer
        return ans