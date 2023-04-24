from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()
        return stones[0] if len(stones) == 1 else 0