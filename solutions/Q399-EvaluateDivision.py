from collections import deque
from typing import List

class Solution:
    class Edge:
        def __init__(self, src, dst, val):
            self.src = src
            self.dst = dst
            self.val = val
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vertexList = {}
        for i in range(len(equations)):
            edgeSrc = self.Edge(equations[i][0], equations[i][1], values[i])
            if edgeSrc.src not in vertexList:
                vertexList[edgeSrc.src] = []
            vertexList[edgeSrc.src].append(edgeSrc)
            edgeDst = self.Edge(equations[i][1], equations[i][0], 1 / values[i])
            if edgeDst.src not in vertexList:
                vertexList[edgeDst.src] = []
            vertexList[edgeDst.src].append(edgeDst)
        for i in range(len(queries)):
            if queries[i][0] not in vertexList or queries[i][1] not in vertexList:
                queries[i] = -1.0
                continue
            if queries[i][0] == queries[i][1]:
                queries[i] = 1.0
                continue
            queue = deque()
            queue.append((queries[i][0], 1.0))
            visited = set()
            visited.add(queries[i][0])
            while queue:
                vertex, val = queue.popleft()
                if vertex == queries[i][1]:
                    queries[i] = val
                    break
                for edge in vertexList[vertex]:
                    if edge.dst not in visited:
                        queue.append((edge.dst, val * edge.val))
                        visited.add(edge.dst)
            if type(queries[i]) != float:
                queries[i] = -1.0
        return queries