from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2): # for the first half of the string
            if s[i] != s[-i - 1]: # if the current character is not the same as the corresponding character from the end
                s[i], s[-i - 1] = s[-i - 1], s[i] # swap the current character with the corresponding character from the end