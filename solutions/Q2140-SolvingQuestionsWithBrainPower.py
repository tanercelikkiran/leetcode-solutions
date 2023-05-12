from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        dp = [0] * len(questions)

        for index, question in enumerate(questions[::-1]):
            contender = question[0] if question[1] >= index else question[0] + dp[index-question[1]-1]
            res = max(res, contender)
            dp[index] = res 
        return res