from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        l = []

        for i in range(len(cost)):
            if i < 2:
                l.append(cost[i])
            else:
                l.append(cost[i] + min(l[i-1], l[i-2]))

        return min(l[-1], l[-2])