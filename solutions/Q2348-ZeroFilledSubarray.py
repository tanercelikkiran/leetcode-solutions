from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total, current = 0, 0 # total number of 0s, current number of 0s

        for num in nums: # for each number in the array
            if num == 0 : # if the number is 0
                current += 1 # increment the current number of 0s
                total += current # add the current number of 0s to the total
            else: # if the number is not 0
                current = 0 # reset the current number of 0s 

        return total # return the total number of 0s