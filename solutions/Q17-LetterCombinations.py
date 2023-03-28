from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits.__len__() == 0:
            return []

        # dictionary of digits and their corresponding letters
        digitDict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        ans = [""] # initialize with empty string

        for d in digits: # for each digit
            temp = [] # temporary list
            for c in digitDict[d]: # for each letter in the digit
                temp += [x + c for x in ans] # append the letter to each string in ans
            ans = temp # update ans
        return ans
    
print(Solution().letterCombinations("23"))