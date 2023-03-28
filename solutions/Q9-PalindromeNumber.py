class Solution:
    def isPalindrome(self, x: int) -> bool:
        strOfX = str(x) # convert x to string
        return strOfX == strOfX[::-1] # return True if strOfX is equal to reverse of string, else return False
    