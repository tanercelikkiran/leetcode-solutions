from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [] # answer
        for i in range(len(nums)): # for each number in nums
            try: # try to find the other number
                j = nums.index(target - nums[i]) # find the other number
                if j != -1 and j != i: # if the other number is found and is not the same number
                    ans.append(i) # add the index of the number to the answer
                    ans.append(j) # add the index of the other number to the answer
                    break # break the loop
            except: # if the other number is not found
                continue # continue the loop
        return ans
