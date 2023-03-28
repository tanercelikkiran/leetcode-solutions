class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 # answer
        i, j = 0, 1 # i is the start of the substring, j is the end of the substring

        if len(s) == 0 or len(s) == 1: # if s is empty or has only one character
            return len(s) # return the length of s

        while j < len(s): # while j is not out of bounds
            if s[j] in s[i:j]: # if s[j] is in the substring
                i += 1 # move i to the next character
            else: # if s[j] is not in the substring
                j += 1 # move j to the next character
                ans = max(ans, j - i) # update the answer
        return ans