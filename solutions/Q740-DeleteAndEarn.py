from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: # if nums is empty
            return 0 # return 0

        max_num = max(nums) # get the max number in nums
        l = [0] * (max_num + 1) # create a list of 0s with length max_num + 1. This is for DP.

        for num in nums: # for each number in nums
            l[num] += num # add the number to the corresponding index in l

        for i in range(2, max_num + 1): # for each index in l starting from 2
            l[i] = max(l[i-1], l[i-2] + l[i]) # set the index to the max of the previous index and the sum of the previous previous index and the current index

        return l[-1] # return the last index in l. This is the max sum.