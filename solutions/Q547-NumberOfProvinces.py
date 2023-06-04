from typing import List

class Solution:
    def union(self, group, i, j):
        group[self.find(group, i)] = self.find(group, j)

    def find(self, group, i):
        if group[i] != i:
            group[i] = self.find(group, group[i])
        return group[i]
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        group = range(len(isConnected))

        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.union(group, i, j)

        return len(set(self.find(group, i) for i in range(n)))

