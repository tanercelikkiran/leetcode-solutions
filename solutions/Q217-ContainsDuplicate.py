from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums) # return True if the length of the set of the list is not equal to the length of the list