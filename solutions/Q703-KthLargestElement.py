from typing import List

class KthLargest:
    nums = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.nums.sort(reverse=True)
        while len(self.nums) > k:
            self.nums.pop()

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort(reverse=True)
        elif val > self.nums[-1]:
            self.nums.pop()
            self.nums.append(val)
            self.nums.sort(reverse=True)
        return self.nums[-1]