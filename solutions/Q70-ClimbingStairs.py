class Solution:
    def climbStairs(self, n: int) -> int:
        n2 = 1 # n = 1
        n1 = 2 # n = 2

        if n == 1 or n == 2:
            return n
        for _ in range(n-2): # for n = 3, 4, 5, ...
            # add n1 and n2 to get n3, n4, n5, ...
            temp = n1 
            n1 = n1+n2
            n2 = temp

        return n1 