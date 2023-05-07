from typing import List

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        stack = []
        for i in range(len(obstacles)):
            if not stack or stack[-1] <= obstacles[i]:
                stack.append(obstacles[i])
                res.append(len(stack))
            else:
                left, right = 0, len(stack) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if stack[mid] <= obstacles[i]:
                        left = mid + 1
                    else:
                        right = mid
                stack[left] = obstacles[i]
                res.append(left + 1)
        return res