from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 # first index of height
        j = len(height) - 1 # last index of height
        ans = 0 # answer
        while i < j: # while i is less than j
            if ans < min(height[i], height[j])*(j-i): # if ans is less than the area of the rectangle
                ans = min(height[i], height[j])*(j-i) # set ans to the area of the rectangle
            if height[i] < height[j]: # if height[i] is less than height[j]
                i += 1 # move i to the right
            else: # if height[i] is greater than or equal to height[j]
                height.pop() # remove height[j] (for size efficiency)
                j -= 1 # move j to the left
        return ans