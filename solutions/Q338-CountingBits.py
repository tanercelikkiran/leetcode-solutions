import math
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1) # answer list
        for i in range(1, n+1): # 0 is special so we start from 1
            if i % 2 ==0: # if i is even
                ans[i] = ans[i//2] # 2^x = 2^(x-1) * 2 so ans[i] = ans[i//2]
            else: # if i is odd
                ans[i] = ans[i//2] + 1 # 2^x = 2^(x-1) * 2 + 1 so ans[i] = ans[i//2] + 1
        return ans