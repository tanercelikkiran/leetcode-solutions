from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0 # carry is 1 if the last digit is 9
        digits[-1] += 1 # add 1 to the last digit
        for i in range(len(digits) - 1, -1, -1): # iterate from the last digit to the first digit
            digits[i] += carry # add the carry to the current digit
            carry = digits[i] // 10 # calculate the carry
            digits[i] %= 10 # calculate the current digit
        if carry: # if there is a carry
            digits.insert(0, carry) # insert the carry to the beginning of the list
        return digits # return the list

    """
    Another solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]    
    """
