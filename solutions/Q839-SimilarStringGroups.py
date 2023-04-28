from typing import List

class Solution:
    def isSimilar(self, s1: str, s2: str) -> bool:
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt > 2:
                    return False
        return True

    def find(self, x: int) -> int:
        if self.group[x] != x:
            self.group[x] = self.find(self.group[x])
        return self.group[x]

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        self.group = [i for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    self.group[self.find(i)] = self.find(j)

        return sum([1 for i in range(n) if self.group[i] == i])