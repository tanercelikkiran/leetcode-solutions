from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = [1] + [0 for i in range(len(target))] # dp[i] means the number of ways to form target[:i]
        for i in range(len(words[0])): # for each column
            countLetter = {} # count the number of each letter in the column
            for word in words: # for each word
                countLetter[word[i]] = countLetter.get(word[i], 0) + 1 # count the number of each letter in the column
            for j in range(len(target)-1, -1, -1): # for each letter in target
                dp[j + 1] += dp[j] * countLetter.get(target[j], 0) % (10**9 + 7) # dp[j + 1] means the number of ways to form target[:j+1]
        return dp[len(target)] % (10**9 + 7)