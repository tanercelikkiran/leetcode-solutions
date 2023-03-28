from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minNum = midNum = 2**31 - 1 # 2**31 - 1 is the max value of 32-bit signed integer

        if len(nums) < 3: # if the length of the list is less than 3
            return False # return False

        for i in nums: # for each number in the list
            if (i < minNum): # if the current number is less than the minimum number
                minNum = i # set the minimum number to the current number
            if (i > minNum): # if the current number is greater than the minimum number
                midNum = i if (i < midNum) else midNum # set the middle number to the current number if the current number is less than the middle number
            if (i > midNum): # if the current number is greater than the middle number
                return True # condition is met, return True
        return False # condition is not met, return False