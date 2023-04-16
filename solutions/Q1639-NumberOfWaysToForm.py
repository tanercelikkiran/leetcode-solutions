from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words) # number of words
        w = len(words[0]) # length of each word
        t = len(target) # length of target
        freq = {i: [0]*26 for i in range(w)} # frequency of each letter in each position
        for i in range(w): # for each position
            for j in range(n): # for each word
                let = ord(words[j][i]) - 97 # get the letter 
                freq[i][let] += 1 # increment the frequency
        dp = [[0]*(w+1) for _ in range(t+1)] # dp[i][j] = number of ways to form target[:i] using words[:j]
        for i in range(w+1): # base case
            dp[0][i] = 1 # there is one way to form an empty string
        for i in range(t): # for each letter in target
            tar = ord(target[i]) - 97 # get the letter
            for j in range(w): # for each position
                num = freq[j][tar] # get the frequency of the letter in the position
                # if the letter is not in the position, then we can't use it
                # if the letter is in the position, then we can use it and the number of ways is dp[i][j]
                dp[i+1][j+1] = (dp[i+1][j] + (dp[i][j]*num) % 1000000007) % 1000000007
        return int(dp[t][w]) # return the number of ways to form target using words 