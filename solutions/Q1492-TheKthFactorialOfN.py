import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        count = 0
        for i in range(1, int(math.sqrt(n)+1)):
            if n%i == 0:
                factors.insert(count, i)
                if n//i not in factors:
                    factors.insert(count+1, n//i)
                    count +=1
        if k > len(factors):
            return -1
        return factors[k-1]
