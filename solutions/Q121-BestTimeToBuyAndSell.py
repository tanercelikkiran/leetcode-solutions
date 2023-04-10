from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.sort()
        return prices[-1] - prices[0]
