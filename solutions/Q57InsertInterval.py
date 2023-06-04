from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key = lambda interval: interval[0])

        i = 0
        n = len(intervals)

        while i < n-1:
            if intervals[i+1][0] > intervals[i][1]:
                i += 1
                continue
            else:
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.remove(intervals[i+1])
                n -= 1
        
        return intervals