from typing import List

class Solution:
    def canJump(self, nums : List[int])-> bool:
        n = len(nums) # length of the array
        pos = 0 # the farthest position that can be reached 
        i = 0  # the current position
        while (i <= pos): # if the current position is reachable 
            pos = max(pos, i + nums[i]) # update the farthest position that can be reached
            if pos >= n - 1:  # if the farthest position is the last position or beyond
                return True  # then return True
            i += 1  # otherwise, move to the next position
        return False # if the current position is not reachable, then return False

print(Solution.canJump([2,3,1,1,4]))