from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()

        ans = 0

        for i in range(1, len(nums)):
            ans = ans if ans > nums[i] - nums[i - 1] else nums[i] - nums[i - 1]

        return ans