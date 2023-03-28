class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": # if needle is empty
            return 0 # return 0

        for i in range(len(haystack) - len(needle) + 1): # iterate through haystack
            if haystack[i:i+len(needle)] == needle: # if the substring of haystack is equal to needle
                return i # return the index of the first character of the substring
        
        return -1 # if needle is not found, return -1