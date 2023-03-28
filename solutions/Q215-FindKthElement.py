from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort() # sort the list
        return nums[-k] # return the kth element from the end of the list
    
    # another solution
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k): # iterate k times
            max = -(10**4) # set the max to the first element
            for j in range(len(nums)): # iterate through the list
                if nums[j] > max: # if the current element is greater than the max
                    max = nums[j] # set the max to the current element
                    index = j # set the index to the current index
            nums.pop(index) # remove the max from the list
        return max # return the max
    """
    