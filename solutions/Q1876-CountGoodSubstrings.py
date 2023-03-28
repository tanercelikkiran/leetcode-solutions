class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0 # number of good substrings
        sList = list(s) # convert string to list

        if len(sList) < 3: # if string is less than 3 characters,
            return 0 # return 0

        for i in range(len(sList) - 2): # iterate through list
            tempSet = set(sList[i:i+3]) # create a set of the current 3 characters
            if len(tempSet) == 3: # if the set has 3 unique characters,
                ans += 1 # increment ans
        
        return ans 