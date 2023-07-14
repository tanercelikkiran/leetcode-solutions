from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = [] # stores the top of each pile
        for i in range(len(nums)): # for each card
            num = nums[i] # get the card
            if len(piles) == 0: # if no piles, start one
                piles.append(num) # start a new pile
                continue # go to next card
            
            if (num > piles[-1]): # if card is greater than top of last pile
                piles.append(num) # start a new pile
            else: # if card is less than or equal to top of last pile
                pos = bisect_left(piles, num) # find the pile to put it in
                piles[pos] = num # put it in the pile
        
        return len(piles)
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18])) # 4