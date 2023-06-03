from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
            def dfs(i, time):
                if i not in children:
                    return time
                return max(dfs(j, time + informTime[i]) for j in children[i])
    
            children = {}
            for i, m in enumerate(manager):
                if m not in children:
                    children[m] = []
                children[m].append(i)
    
            return dfs(headID, 0)