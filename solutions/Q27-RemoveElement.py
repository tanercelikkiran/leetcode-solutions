from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums: # while val in nums is True
            nums.remove(val) # remove the first occurrence of val