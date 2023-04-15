import functools
from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @functools.lru_cache(None) # cache the result of func(i, k)
        def func(i, k): # the maximum value of k coins from piles[i:]
            if k == 0 or i == len(piles): return 0 # no more coins or no more piles
            res, cur = func(i + 1, k), 0 # not take the first coin of the current pile
            for j in range(min(len(piles[i]), k)): # take the first j coins of the current pile
                cur += piles[i][j] # add the value of the first j coins
                res = max(res, cur + func(i+1, k-j-1)) # add the value of the remaining coins
            return res # return the maximum value of k coins from piles[i:]
        return func(0, k)