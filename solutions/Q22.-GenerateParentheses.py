from typing import List

class Solution:
    def generate(self, ans: List[int], left: int, right: int, n: int, s: str) -> None:
        if right == n: # if right is equal to n, then we have a valid string
            ans.append(s) # add it to the answer
            return # and return
        if left < n: # if left is less than n, then we can add a left parenthesis
            self.generate(ans, left + 1, right, n, s + '(') # add a left parenthesis
        if right < left: # if right is less than left, then we can add a right parenthesis
            self.generate(ans, left, right + 1, n, s + ')') # add a right parenthesis

    def generateParenthesis(self, n: int) -> List[str]: 
        ans = [] # initialize the answer
        self.generate(ans, 0, 0, n, '') # call the recursive function
        return ans