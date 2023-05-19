from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        #DFS based stack solution

        # 0: unvisited
        # 1: group 1
        # 2: group 2
        visited = [0] * len(graph)

        stack = []

        for i in range(len(graph)):
            if visited[i] == 0:
                stack = [i]
                visited[i] = 1

                while stack:
                    node = stack.pop()

                    for neighbor in graph[node]:
                        if visited[neighbor] == visited[node]:
                            return False
                        elif visited[neighbor] == 0:
                            stack.append(neighbor)
                            visited[neighbor] = 3 - visited[node]

        return True