from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # Since the majority element is more than half of the array,
        # the middle element must be the majority element.
        return nums[len(nums)//2]