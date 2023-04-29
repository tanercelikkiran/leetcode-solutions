from typing import List

class UnionFind:
    def __init__(self, edgeList):
        self.parent = {x[0]: x[0] for x in edgeList}
        self.count = len(edgeList)

    # Time: O(logn) | Space: O(1)
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    # Time: O(1) | Space: O(1)
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        # already in the same set
        if root1 == root2:
            return
        if self.count[root1] < self.count[root2]:
            self.parent[root1] = root2
            self.count[root2] += self.count[root1]
        else:
            self.parent[root2] = root1
            self.count[root1] += self.count[root2]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []

        for i in range(len(queries)):
            limitedEdges = [edge for edge in edgeList if edge[2] < queries[i][2]]
            uf = UnionFind(limitedEdges)
            res.append(uf.find(queries[i][0]) == uf.find(queries[i][1]))

        return res
