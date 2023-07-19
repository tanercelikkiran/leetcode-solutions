from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # sort the intervals by the end time
        res = 0 # result
        prev = float('-inf') # previous end time
        for interval in intervals: # iterate through the intervals
            if interval[0] >= prev: # if the start time is greater than or equal to the previous end time
                prev = interval[1] # update the previous end time
            else: # if the start time is less than the previous end time
                res += 1 # increment the result
        return res # return the result