from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        initial = 0 # initial number of zeros
        ans = 0 # number of subarrays

        for i in range(len(nums)):
            if nums[i] == 0: # if the current number is zero
                initial += 1 # increase the initial number of zeros
                ans += initial # add the initial number of zeros to the answer
            else: # if the current number is not zero
                initial = 0 # reset the initial number of zeros
        return ans