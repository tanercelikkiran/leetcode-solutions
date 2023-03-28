from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0 # number of arithmetic triplets
        for i in range(len(nums)): # for each number in the list
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums: # if the current number plus the difference is in the list and the current number plus twice the difference is in the list
                ans += 1 # increase the number of arithmetic triplets
        return ans # return the number of arithmetic triplets