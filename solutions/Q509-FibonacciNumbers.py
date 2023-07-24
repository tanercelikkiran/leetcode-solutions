class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return 1 if n else 0
        a, b = 0, 1
        for _ in range(n-2):
            a, b= b, a+b
        return b