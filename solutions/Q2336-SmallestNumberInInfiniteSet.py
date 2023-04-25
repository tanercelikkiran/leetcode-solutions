class SmallestInfiniteSet:
    nums = []

    def __init__(self):
        self.nums = [i for i in range(1, 1000)]

    def popSmallest(self) -> int:
        return self.nums.pop(0)

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.append(num)
            self.nums.sort()