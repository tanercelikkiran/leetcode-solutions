class Solution:
    def climbStairs(self, n: int) -> int:
        n2 = 1 # the number of ways to climb n-2 stairs
        n1 = 2 # the number of ways to climb n-1 stairs

        if n == 1 or n == 2: # if there is only 1 or 2 stairs, there is only 1 way to climb
            return n
        for _ in range(n-2): # for each stair from n-2 to 1
            temp = n1 # store the number of ways to climb n-1 stairs
            n1 = n1+n2 # the number of ways to climb n stairs is the number of ways to climb n-1 stairs plus the number of ways to climb n-2 stairs
            n2 = temp # the number of ways to climb n-2 stairs is the number of ways to climb n-1 stairs

        return n1