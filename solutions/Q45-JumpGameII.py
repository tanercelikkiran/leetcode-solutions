from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 # number of jumps
        l = r = 0 # left and right boundaries of current jump

        while r < len(nums) - 1: # if r is the last index, we don't need to jump anymore
            farthest = 0 # farthest index we can reach in the next jump
            for i in range(l, r + 1): # for each index in the current jump
                farthest = max(i + nums[i], farthest) # update farthest index
            l = r + 1 # next jump's left boundary is the current jump's right boundary + 1
            r = farthest # next jump's right boundary is the farthest index we can reach
            res += 1 # update number of jumps
        return res
