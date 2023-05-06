from typing import List

class Solution:
    # When we find the maximum number that can be the rightmost number in a subsequence, 
    # we can count the number of subsequences. Since the minimum number is fixed,
    # we can choose any number from the left side of the maximum number. 
    # Then we have to sum up these subsequence numbers.
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort() # sort the array
        l, r = 0, len(nums) - 1 # two pointers
        res = 0 # result
        while l <= r: # while right pointer is greater than left pointer
            if nums[l] + nums[r] > target: # if the sum of the two pointers is greater than target
                r -= 1 # decrement right pointer and try again
            else: # if the sum of the two pointers is less than or equal to target
                res += 2 ** (r - l) # add the total number of subsequences from l to r to the result
                l += 1 # increment left pointer and try again to find more subsequences
        return res % (10 ** 9 + 7)