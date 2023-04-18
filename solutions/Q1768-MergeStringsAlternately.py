class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1) , len(word2)) # get the length of the shortest string
        st = "" # initialize the string
        for i in range(n): # loop through the shortest string
            st += word1[i] + word2[i] # add the characters from both strings
        return st+word1[n:]+word2[n:] # add the remaining characters from the longer string